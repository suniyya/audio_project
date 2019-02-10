from watson_segment_sentence import get_words_from_audio

def initialize(json_obj):
    sentenceInfo = json_obj['results'][0]['alternatives'][0]
    sentence = sentenceInfo['transcript']
    words = sentenceInfo['timestamps'] # lists of three: word, start, end
    confidence = sentenceInfo['confidence']
    snippet = {
        'sentence': sentence,
        'words': words,
        'confidence': confidence
    }
    return snippet

def lengthTest(prior, current):
    # return 0 for fail, 1 for pass
    pauseLengthCurrentSample = sum([current['words'][i+1][1]-current['words'][i][2] for i in range(0, len(current['words'])-1)])
    pauseLengthPriorSample = sum([prior['words'][i+1][1]-prior['words'][i][2] for i in range(0, len(prior['words'])-1)])
    if pauseLengthCurrentSample-pauseLengthPriorSample > 1.5:
        return 0
    totalLengthCurrentSample = current['words'][-1][1] - current['words'][0][1]
    totalLengthPriorSample = prior['words'][-1][1] - prior['words'][0][1]
    if totalLengthCurrentSample > 1.5*totalLengthPriorSample or totalLengthCurrentSample < 0.667*totalLengthPriorSample:
        return 0
    else:
        return 1

def wordsEquality(current, prior):
    # returns 0 if obvious numMismatch
    # returns 1 if all the words match and are in order
    # returns a number between 0 and 1 if a fraction of words match. fraction correct is returned.
    numMismatches = 0
    if len(current['words']) != len(prior['words']):
        return 0
    else:
        for i in range(len(current['words'])):
            if current['words'][i][0] != prior['words'][i][0]:
                print current['words'][i][0]
                print prior['words'][i][0]
                numMismatches += 1.0
        return 1 - numMismatches/len(current['words'])

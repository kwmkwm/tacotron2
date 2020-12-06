import re

_letters = "abcdefghijklmnopqrstuvwxyz'"
_punctuation = " ,.!?"
_vocab = _letters + _punctuation + "{}"
phonemes = ['PAD', 'EOS'] + ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1', 'AH2',
                             'AO0', 'AO1', 'AO2', 'AW0', 'AW1', 'AW2', 'AY0', 'AY1', 'AY2',
                             'B', 'CH', 'D', 'DH',
                             'EH0', 'EH1', 'EH2', 'ER0', 'ER1', 'ER2', 'EY0', 'EY1', 'EY2',
                             'F', 'G', 'HH', 'IH0', 'IH1', 'IH2', 'IY0', 'IY1', 'IY2', 'JH',
                             'K', 'L', 'M', 'N', 'NG', 'OW0', 'OW1', 'OW2', 'OY0', 'OY1', 'OY2',
                             'P', 'R', 'S', 'SH', 'T', 'TH',
                             'UH0', 'UH1', 'UH2', 'UW', 'UW0', 'UW1', 'UW2',
                             'V', 'W', 'Y', 'Z', 'ZH'] + list(_punctuation)


#re-using code from a previous project, what could go wrong?
def _text_normalize(text):

    text = text.replace('-', ' ')
    # pauses are pauses, right?
    text = text.replace(';', ',')
    # but maybe some pauses are longer than others?
    text = text.replace(':', '.')
    text = text.lower()
    # if its not in the _vocab list change it to a space
    text = re.sub("[^{}]".format(_vocab), " ", text)
    # change multiple spaces to single spaces
    text = re.sub("[ ]+", " ", text)
    # remove blank characters from beginning and end
    text = text.strip()
    return text


def _phoneme_normalize(phones,verbose=False):
    pre_processed_phones = []
    processed_phones = []
    # remove unwanted characters
    for phone in phones:
        if (phone in phonemes):
            pre_processed_phones.append(phone)
        else:
            if verbose:
                print("dropping unexpected phone")
                print(phone)

    # G2p adds spaces before punctuation
    # lets remove them
    for idx, p_phone in enumerate(pre_processed_phones):
        if not p_phone == ' ':
            processed_phones.append(p_phone)
        else:
            if idx + 1 < len(pre_processed_phones):
                if not (pre_processed_phones[idx + 1] in _punctuation):
                    processed_phones.append(p_phone)
                else:
                    if verbose:
                        print("dropping unnecessary space")
            else:
                if verbose:
                    print("dropping dangling space")

    return processed_phones

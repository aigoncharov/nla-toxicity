from convokit import Corpus
import pathlib

WORD_MIN_COUNT = 8
CHAR_MIN_COUNT = 30
LINE_COUNT = 500


def count_words(text):
    return len(text.strip().split(" "))


def count_chars(text):
    return len(text)


def get_prompts():
    corpus = Corpus(str(pathlib.Path(__file__).parent.joinpath("data").resolve()))
    corpus.print_summary_stats()

    conversations = []

    for convo in corpus.iter_conversations():
        conversation_text = ""
        conversation_word_count = 0
        conversation_char_count = 0

        for utt in convo.iter_utterances():
            if utt.speaker.id == "AutoModerator":
                continue

            conversation_text += utt.text + " "
            conversation_word_count += count_words(utt.text)
            conversation_char_count += count_chars(utt.text)

            if conversation_word_count > WORD_MIN_COUNT and conversation_char_count > CHAR_MIN_COUNT:
                break

        if conversation_word_count > WORD_MIN_COUNT and conversation_char_count > CHAR_MIN_COUNT:
            words = conversation_text.strip().split(" ")
            fin = ""
            for word in words:
                fin += word + " "
                if count_chars(fin) > CHAR_MIN_COUNT:
                    break
            conversations.append(fin)

        if len(conversations) == LINE_COUNT:
            break

    return conversations

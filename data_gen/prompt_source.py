from convokit import Corpus, download

WORD_MIN_COUNT = 10
CHAR_MIN_COUNT = 50
# Match paper
LINE_COUNT = 24576


def count_words(text):
    return len(text.strip().split(" "))


def is_english_letter(char):
    return char.isalpha() and ord(char) < 128


def count_chars(text):
    cnt = 0
    for c in text:
        if is_english_letter(c):
            cnt += 1
    return cnt


def get_prompts():
    corpus = Corpus(download("movie-corpus"))
    corpus.print_summary_stats()

    conversations = []

    for convo in corpus.iter_conversations():
        conversation_text = ""
        conversation_word_count = 0
        conversation_char_count = 0

        for utt in convo.iter_utterances():
            conversation_text += utt.text + " "
            conversation_word_count += count_words(utt.text)
            conversation_char_count += count_chars(utt.text)

            if (
                conversation_word_count > WORD_MIN_COUNT
                and conversation_char_count > CHAR_MIN_COUNT
            ):
                break

        if (
            conversation_word_count > WORD_MIN_COUNT
            and conversation_char_count > CHAR_MIN_COUNT
        ):
            conversations.append(conversation_text)

        if len(conversations) == LINE_COUNT:
            break

    return conversations

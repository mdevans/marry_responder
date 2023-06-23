# Foondamate Coding Challenge (https://careers.foondamate.com/machine-learning-engineer-remote/foondamate-ml-engineer-coding-challenge-001)

## Nltk_stemmer Classifier Performance:

              precision    recall  f1-score   support

         ask       1.00      0.97      0.99        36
      shared       0.98      0.98      0.98        47
     unclear       0.90      0.95      0.93        20

    accuracy                           0.97       103
    macro avg      0.96      0.97      0.96       103
    weighted avg   0.97      0.97      0.97       103

Incorrectly classified phrases:
Phrase: 'The email you provided is recorded', Predicted: 'shared', Actual: 'unclear'
Phrase: 'Your email is now with my roommate hope its okay', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Can my classmates email you too', Predicted: 'unclear', Actual: 'ask'

## Nltk_lemma Classifier Performance:

              precision    recall  f1-score   support

         ask       1.00      0.97      0.99        36
      shared       0.98      0.98      0.98        47
     unclear       0.90      0.95      0.93        20

    accuracy                           0.97       103
    macro avg      0.96      0.97      0.96       103
    weighted avg   0.97      0.97      0.97       103

Incorrectly classified phrases:
Phrase: 'The email you provided is recorded', Predicted: 'shared', Actual: 'unclear'
Phrase: 'Your email is now with my roommate hope its okay', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Can my classmates email you too', Predicted: 'unclear', Actual: 'ask'

## Nltk_pos_tag Classifier Performance:

              precision    recall  f1-score   support

         ask       1.00      0.00      0.00        36
      shared       1.00      0.00      0.00        47
     unclear       0.19      1.00      0.33        20

    accuracy                           0.19       103
    macro avg      0.73      0.33      0.11       103
    weighted avg   0.84      0.19      0.06       103

Incorrectly classified phrases:
<TOO MANY>

## Hf_zero_shot Classifier Performance:

              precision    recall  f1-score   support

         ask       1.00      0.89      0.94        36
      shared       0.92      0.94      0.93        47
     unclear       0.87      1.00      0.93        20

    accuracy                           0.93       103
    macro avg      0.93      0.94      0.93       103
    weighted avg   0.94      0.93      0.93       103

Incorrectly classified phrases:
Phrase: 'Might I share your email', Predicted: 'shared', Actual: 'ask'
Phrase: 'Could we share your email address with my friends', Predicted: 'shared', Actual: 'ask'
Phrase: 'May we pass on your email to our associates', Predicted: 'shared', Actual: 'ask'
Phrase: 'I've included your email in our group discussion', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Your email has been included in the meeting agenda', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Your email has been added to the mailing list', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Can my classmates email you too', Predicted: 'shared', Actual: 'ask'

## Openai_davinci Classifier Performance:

              precision    recall  f1-score   support

         ask       0.90      0.97      0.93        36
      shared       1.00      0.45      0.62        47
     unclear       0.47      1.00      0.63        20

    accuracy                           0.74       103
    macro avg      0.79       0.81     0.73       103
    weighted avg   0.86       0.74     0.73       103

Incorrectly classified phrases:
Phrase: 'I've sent your email address to my friend', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I shared your digits', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I have sent this email to my friends', Predicted: 'unclear', Actual: 'shared'
Phrase: 'The email has been shared with all my friends', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I forwarded your email to a colleague', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Just forwarding your email', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Forwarded your email for review', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Giving your contact details to someone', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I've given your email address', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Distributed your email among the team', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I've included your email in our group discussion', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Including your email in the company newsletter', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Your email has been included in the meeting agenda', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Circulating your email among the stakeholders', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Just circulating your email', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Just passing along your email', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Passing your email to the customer support team', Predicted: 'ask', Actual: 'shared'
Phrase: 'Adding your email to the distribution list', Predicted: 'ask', Actual: 'shared'
Phrase: 'Your email has been added to the mailing list', Predicted: 'ask', Actual: 'shared'
Phrase: 'Your email is now with my roommate hope its okay', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I have forwarded your email to my lab partner', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Passed your email to my classmates thank you', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Ive given your email to a friend who needs help', Predicted: 'unclear', Actual: 'shared'
Phrase: 'I have given your email to a friend thanks', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Can my classmates email you too', Predicted: 'unclear', Actual: 'ask'
Phrase: 'Shared your email with my seminar group', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Ive shared your email with others hope its okay', Predicted: 'ask', Actual: 'shared'

## Openai_gpt35 Classifier Performance:

              precision    recall  f1-score   support

         ask       0.97      1.00      0.99        36
      shared       0.91      0.89      0.90        47
     unclear       0.80      0.80      0.80        20

    accuracy                           0.91       103
    macro avg      0.90      0.90      0.90       103
    weighted avg   0.91      0.91      0.91       103

Incorrectly classified phrases:
Phrase: 'I have sent this email to my friends', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Giving your contact details to someone', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Including your email in the company newsletter', Predicted: 'ask', Actual: 'shared'
Phrase: 'Your email has been included in the meeting agenda', Predicted: 'unclear', Actual: 'shared'
Phrase: 'Adding your email to the distribution list', Predicted: 'unclear', Actual: 'shared'
Phrase: 'We have your email on file', Predicted: 'shared', Actual: 'unclear'
Phrase: 'Your email is in the database', Predicted: 'shared', Actual: 'unclear'
Phrase: 'We have your contact details', Predicted: 'shared', Actual: 'unclear'
Phrase: 'We've captured your email address', Predicted: 'shared', Actual: 'unclear'

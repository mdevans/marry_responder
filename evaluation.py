# Purpose: Contains functions for evaluating the performance of classifiers.
from sklearn.metrics import classification_report


def evaluate_classifier(
    classifier_name: str,
    phrases: list[str],
    labels: list[str],
    predictions: list[str],
) -> None:
    print(f"\n{classifier_name} Performance:\n")
    print(classification_report(labels, predictions, zero_division=1))

    incorrect_predictions = [
        f"Phrase: '{phrases[i]}', Predicted: '{predictions[i]}', Actual: '{labels[i]}'"
        for i in range(len(labels))
        if labels[i] != predictions[i]
    ]

    print("\nIncorrectly classified phrases:")
    for incorrect in incorrect_predictions:
        print(incorrect)

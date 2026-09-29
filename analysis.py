import pandas as pd


def average(df, column):
    return df[column].mean()


def percentage_change(old_value, new_value):
    if old_value == 0:
        raise ValueError("Cannot calculate percentage change from zero.")

    return ((new_value - old_value) / old_value) * 100


def correlation(df, column_x, column_y):
    return df[column_x].corr(df[column_y])


def outlier_detection(df, column):
    mean = df[column].mean()
    std = df[column].std()

    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std

    return df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]


def run_analysis(operation, df, **kwargs):

    if operation == "AVERAGE":
        return average(
            df,
            kwargs["column"]
        )

    elif operation == "PERCENTAGE_CHANGE":
        return percentage_change(
            kwargs["old_value"],
            kwargs["new_value"]
        )

    elif operation == "CORRELATION":
        return correlation(
            df,
            kwargs["column_x"],
            kwargs["column_y"]
        )

    elif operation == "OUTLIER_DETECTION":
        return outlier_detection(
            df,
            kwargs["column"]
        )

    else:
        raise ValueError(
            f"Unsupported analysis operation: {operation}"
        )
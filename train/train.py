import tensorflow as tf
from tensorflow.keras import layers, Input, Model
import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--hidden_units", type=int, required=True)
    parser.add_argument("--optimizer", type=str, required=True)
    args = parser.parse_args()
    return args


def train(hidden_units, optimizer):
    (train_x, train_y), (test_x, test_y) = tf.keras.datasets.mnist.load_data()
    train_x = train_x / 255.0
    test_x = test_x / 255.0

    inputs = Input(shape=(28, 28))
    x = layers.Flatten()(inputs)
    x = layers.Dense(hidden_units, activation="relu")(x)
    outputs = layers.Dense(10, activation="softmax")(x)

    model = Model(inputs, outputs)

    optimizer = tf.keras.optimizers.get(optimizer)

    model.compile(
        optimizer=optimizer, loss="sparse_categorical_crossentropy", metrics=["acc"]
    )
    model.fit(train_x, train_y, epochs=3, validation_split=0.2)
    loss, acc = model.evaluate(test_x, test_y)
    print(f"model test-loss={loss:.4f} test-acc={acc:.4f}")


if __name__ == "__main__":
    args = get_args()
    train(args.hidden_units, args.optimizer)

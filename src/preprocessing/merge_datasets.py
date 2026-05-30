import pandas as pd
from pathlib import Path

# Equivalente a hacer: cd .. y luego cd ..
base_path = Path(__file__).parent.parent.parent

raw_path = base_path / "data" / "raw"
clean_path = base_path / "data" / "clean"

train_df = pd.read_csv(raw_path / "training.csv")
val_df = pd.read_csv(raw_path / "validation.csv")
test_df = pd.read_csv(raw_path / "test.csv")

df_completo = pd.concat([train_df, val_df, test_df], ignore_index=True)

df_completo.to_csv(
    clean_path / "emotion_dataset.csv",
    index=False
)

print("Dataset unificado correctamente.")
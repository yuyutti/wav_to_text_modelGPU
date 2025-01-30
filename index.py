import whisper
import os

# WhisperモデルをGPUでロード
model = whisper.load_model("small", device="cuda")

# 対象ディレクトリ（今のディレクトリ）
input_dir = "C:/Users/yuyutti/Desktop/sound to text"

# ファイルリストを取得
for file in os.listdir(input_dir):
    if file.endswith((".wav", ".mp3", ".m4a", ".flac", ".ogg", ".aac")):  # 対応する音声形式
        file_path = os.path.join(input_dir, file)
        print(f"処理中: {file_path}")

        # 音声をWhisperで文字起こし
        result = model.transcribe(file_path, language="ja")

        # 出力ファイル名（拡張子をTXTに）
        output_txt = os.path.splitext(file_path)[0] + ".txt"

        # テキストファイルに保存
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"完了: {output_txt}")

print("すべてのファイルの変換が完了しました！")

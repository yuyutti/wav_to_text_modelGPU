# wav_to_text_modelGPU
pyとGPU使って音声ファイルから字幕テキスト生成するコード GPUの手順もせっかくだから記録残しとく


ffmpeg経由でm3u8を取ってくる場合
ffmpeg -i "m3u8URL" -map 0:a -acodec pcm_s16le -ar 16000 -ac 1 audio.wav

実行前に
pip install openai-whisper
pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

Pythonはマジ分からん、今回GPU使うためにpy使ったけどGPT任せだからAIの仰せのままにって感じ

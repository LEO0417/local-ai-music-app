from flask import Flask, render_template, request
import os
import time

from src.models.musicgen import MusicGen
from src.utils.device import get_optimal_device

app = Flask(__name__)

# 缓存不同模型的生成器，避免重复加载
_generators = {}


def get_generator(model_size: str) -> MusicGen:
    if model_size not in _generators:
        device, _ = get_optimal_device()
        _generators[model_size] = MusicGen(model_size=model_size, device=device)
    return _generators[model_size]


@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        model_size = request.form.get('model', 'small')
        max_tokens = request.form.get('max_tokens')
        max_tokens = int(max_tokens) if max_tokens else None

        generator = get_generator(model_size)

        # 在static目录下保存生成的音频
        filename = f"music_{model_size}_{int(time.time())}.wav"
        output_path = os.path.join('static', filename)

        generator.generate(
            prompt=prompt,
            max_tokens=max_tokens,
            output_path=output_path
        )

        audio_file = filename

    return render_template('index.html', audio_file=audio_file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


from pathlib import Path
from flask import Flask, render_template, request, url_for

from src.models.musicgen import MusicGen
from src.utils.device import get_optimal_device

app = Flask(__name__)

STATIC_DIR = Path(__file__).parent / "static"
STATIC_DIR.mkdir(exist_ok=True)

# 创建MusicGen实例和设备
DEVICE, DEVICE_NAME = get_optimal_device()
print(f"使用设备: {DEVICE_NAME}")
GENERATOR = MusicGen(model_size="small", device=DEVICE)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt", "")
    model = request.form.get("model", "small")
    max_tokens = request.form.get("max_tokens")
    try:
        max_tokens = int(max_tokens) if max_tokens else None
    except ValueError:
        max_tokens = None

    # 如果模型大小改变，重新创建生成器
    global GENERATOR
    if GENERATOR.model_size != model:
        GENERATOR = MusicGen(model_size=model, device=DEVICE)

    output_path = STATIC_DIR / f"generated_{model}.wav"
    filename = GENERATOR.generate(prompt, max_tokens=max_tokens, output_path=str(output_path))
    # 将文件名相对于static目录返回
    rel_name = Path(filename).name
    return render_template("result.html", filename=rel_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

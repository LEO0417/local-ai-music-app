# AI音乐生成应用 v2.0 (模块化版)

这是一个基于Facebook MusicGen模型的AI音乐生成应用，采用模块化设计，支持small和medium模型，可以根据文本描述生成高质量音乐。

## 🎯 功能特点

- **多模型支持**: 支持MusicGen-small和MusicGen-medium模型
- **智能设备选择**: 自动选择最优计算设备（MPS/CUDA/CPU）
- **模块化设计**: 清晰的代码结构，易于理解和扩展
- **高质量输出**: 生成32kHz采样率的高质量WAV文件
- **灵活配置**: 支持自定义参数和输出路径

## 📁 项目结构

```
local-ai-music-app/
├── src/                    # 源代码目录
│   ├── __init__.py        # 标记src为Python包
│   ├── models/            # 模型相关代码
│   │   ├── __init__.py    # 标记models为Python包
│   │   └── musicgen.py    # MusicGen模型的核心实现
│   ├── utils/             # 工具函数
│   │   ├── __init__.py    # 标记utils为Python包
│   │   └── device.py      # 设备选择工具
│   └── main.py            # 主程序入口
├── app.py                 # 旧版本的主程序（已重构）
├── app_old.py             # 原始版本的备份
└── requirements.txt       # 项目依赖列表
```

## 📦 安装

### 系统要求

- Python 3.8+
- PyTorch 2.0+
- 内存要求:
  - Small模型: 4GB+
  - Medium模型: 8GB+
- 存储空间: 10GB+（用于模型缓存）

### 安装依赖

```bash
pip install -r requirements.txt
```

## 🚀 使用方法

### 基本使用

```bash
# 进入src目录
cd src

# 使用small模型（默认）
python main.py

# 使用medium模型
python main.py --model medium

# 自定义提示词
python main.py --prompt "A peaceful piano melody with soft strings"

# 指定输出文件
python main.py --output my_music.wav
```

### 启动Web界面

```bash
# 在项目根目录
python web_app.py
# 浏览器访问 http://localhost:8000
```

### 高级选项

```bash
# 使用medium模型生成更长的音乐
python main.py --model medium --max-tokens 1024

# 生成电子舞曲
python main.py --model medium --prompt "An energetic electronic dance track with heavy bass and synthesizers"

# 生成爵士乐
python main.py --model medium --prompt "A smooth jazz piece with saxophone, piano, and walking bass"
```

### 查看帮助

```bash
python main.py --help
```

## 📚 代码说明

### 文件作用详解

#### 1. `src/__init__.py`
- **作用**: 标记src目录为Python包
- **内容**: 包的文档说明和使用示例

#### 2. `src/models/__init__.py`
- **作用**: 标记models目录为Python包
- **内容**: 模型包的文档说明

#### 3. `src/utils/__init__.py`
- **作用**: 标记utils目录为Python包
- **内容**: 工具包的文档说明

#### 4. `src/utils/device.py`
- **作用**: 设备选择工具
- **功能**: 
  - 检测可用的计算设备（MPS/CUDA/CPU）
  - 按优先级选择最优设备
  - 返回设备对象和描述信息

#### 5. `src/models/musicgen.py`
- **作用**: MusicGen模型的核心实现
- **功能**:
  - 模型加载和初始化
  - 文本处理和音频生成
  - 音频文件保存
  - 支持small和medium两种模型

#### 6. `src/main.py`
- **作用**: 主程序入口
- **功能**:
  - 命令行参数解析
  - 程序流程控制
  - 错误处理

## 🎛️ 模型对比

| 特性 | Small | Medium |
|------|-------|--------|
| 参数数量 | 300M | 1.5B |
| 模型文件 | ~2.5GB | ~6-8GB |
| 内存需求 | 4GB+ | 8GB+ |
| 加载时间 | 30-60秒 | 2-5分钟 |
| 生成质量 | 良好 | 优秀 |
| 生成速度 | 快 | 中等 |
| 推荐用途 | 快速原型 | 高质量输出 |

## ⚙️ 配置选项

### 命令行参数

- `--prompt`: 音乐描述文本
- `--model`: 模型选择 (small/medium)
- `--output`: 输出文件路径
- `--max-tokens`: 最大生成token数

### 环境变量

- `HF_HOME`: Hugging Face缓存目录
- `TORCH_DEVICE`: 强制指定计算设备

## 🔧 开发指南

### 运行测试

```bash
# 测试设备选择
cd src/utils
python device.py

# 测试模型加载
cd src/models
python musicgen.py

# 测试完整流程
cd src
python main.py --model small --prompt "Test melody"
```

### 代码结构说明

#### 模块化设计的好处：
1. **可维护性**: 每个模块职责单一，易于修改和调试
2. **可扩展性**: 可以轻松添加新的模型或工具
3. **可重用性**: 模块可以在其他项目中复用
4. **可测试性**: 每个模块可以独立测试

#### 导入关系：
```
main.py
├── models.musicgen.MusicGen
└── utils.device.get_optimal_device

musicgen.py
├── transformers (外部库)
├── torch (外部库)
└── scipy (外部库)

device.py
└── torch (外部库)
```

## 📝 示例

### 生成不同类型的音乐

```bash
# 古典音乐
python main.py --model medium --prompt "A beautiful classical symphony with strings and woodwinds"

# 摇滚乐
python main.py --model medium --prompt "An energetic rock song with electric guitar and drums"

# 环境音乐
python main.py --model medium --prompt "Ambient electronic music with atmospheric pads and gentle rhythms"

# 民谣
python main.py --model medium --prompt "A gentle folk song with acoustic guitar and harmonica"
```

## 🐛 故障排除

### 常见问题

1. **内存不足**
   - 使用small模型
   - 减少max-tokens参数
   - 关闭其他应用程序

2. **模型下载慢**
   - 使用稳定的网络连接
   - 考虑使用镜像源

3. **设备兼容性**
   - 确保PyTorch版本正确
   - 检查CUDA/MPS支持

4. **导入错误**
   - 确保在src目录下运行
   - 检查Python路径设置

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 支持

如有问题，请创建Issue或联系开发者。

## 🔄 版本历史

- **v2.0**: 模块化重构，支持medium模型
- **v1.0**: 基础功能实现 
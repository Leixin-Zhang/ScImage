
## ScImage: How good are multimodal large language models at scientific text-to-image generation?



<div align="center",style="font-family: charter;">
    <a href="https://scholar.google.com/citations?user=dTRy2gUAAAAJ&hl=en" target="_blank">Leixin Zhang</a>,
    <a href="https://scholar.google.com/citations?user=TnuqAW0AAAAJ&hl=en" target="_blank">Steffen Eger</a>,
    <a href="https://openreview.net/profile?id=~Yinjie_Cheng1" target="_blank">Yinjie Cheng</a>,
    <a href="https://scholar.google.com/citations?user=0BU245kAAAAJ&hl=en" target="_blank">Weihe Zhai</a>,
    <a href="https://scholar.google.com/citations?user=ut5IWKwAAAAJ&hl=en" target="_blank">Jonas Belouadi</a>,
    <a href="https://scholar.google.com/citations?user=UxfiZA0AAAAJ&hl=en" target="_blank">Fahimeh Moafian</a>,
    <a href="https://scholar.google.com/citations?user=bwiMxxsAAAAJ&hl=en" target="_blank">Zhixue Zhao</a>
</div>


#### 🔥 News: **ScImage Accepted at ICLR 2025** <a href="https://huggingface.co/datasets/casszhao/ScImage" target="_blank"> <img alt="Benchmark: ScImage" src="https://img.shields.io/badge/%F0%9F%A4%97%20_Benchmark-ScImage-ffc107?color=ffc107&logoColor=white" height="15"/> </a>


    
### 🚀 Introduction: 
ScImage——a **benchmark** designed to evaluate the multimodal capabilities of LLMs in **scientific image generation** from textual descriptions. 
- ScImage assesses **three dimensions of understanding**: spatial, numeric, and attribute comprehension, as well as their combinations.
- We evaluate **seven models**: GPT-4o, Llama, AutomaTikZ, Dall-E, StableDiffusion, GPT-o1 and Qwen2.5-Coder-Instruct
- Two modes of output generation: **code-based outputs (Python, TikZ)** and direct **raster image generation**.
- Multilingual: we examine **four different input languages**: English, German, Farsi, and Chinese.

### 📝 Prompt & Template:
- [Template](template.csv): 101 templates with replacable features within `{feature}`.
- [English Prompts](prompt.csv): 404 English prompts for model evaluation.
- [Multilingual Prompts](multilingual_prompt.csv): 20 prompts (covering all understanding dimensions) are translated to other three languages: German, Farsi, and Chinese.

    
**Generation Mode:**

- Text-Code-Image:
    - python: Please generate a scientific figure according to the following requirements: `{generation query}`. Your output should be in Python code. Do not include any text other than the Python code.
    - tikz: Please generate a scientific figure according to the following requirements: `{generation query}`. Your output should be in Tikz code. Do not include any text other than the Tikz code.
- Text-Image: Please generate a scientific figure according to the following requirements: `{generation query}`.
  
### Generation Output

Code Output: 
- [Code generation with English prompts](https://drive.google.com/drive/folders/17QPqBBCGMW1gL4t63T_3h-G02NrgsyQS?usp=sharing)
- [Code generation with multilingual prompts](https://drive.google.com/drive/folders/1vYaRGRd6XvcT2pjZYQ2w76-b57arPGVZ?usp=sharing)

Image Output: 
- [Image generation with English prompts](https://drive.google.com/drive/folders/1Ruj0XihQylbpORBDLWrRAC8OIb0zLORY?usp=sharing)
- [Image generation with multilingual prompts](https://drive.google.com/drive/folders/1Ke2oL2nmXwpSSwZfh_yifyAof_XYlIGo?usp=sharing)


### Human evaluation scores: 



## Citation 
```
@article{zhang2024scimage,
  title={ScImage: How Good Are Multimodal Large Language Models at Scientific Text-to-Image Generation?},
  author={Zhang, Leixin and Eger, Steffen and Cheng, Yinjie and Zhai, Weihe and Belouadi, Jonas and Leiter, Christoph and Ponzetto, Simone Paolo and Moafian, Fahimeh and Zhao, Zhixue},
  journal={arXiv preprint arXiv:2412.02368},
  year={2024}
}
```


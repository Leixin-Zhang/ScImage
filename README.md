
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
- [Code output (English)](https://drive.google.com/drive/folders/17QPqBBCGMW1gL4t63T_3h-G02NrgsyQS?usp=sharing)
- [Code output (multilingual)](https://drive.google.com/drive/folders/1vYaRGRd6XvcT2pjZYQ2w76-b57arPGVZ?usp=sharing)

Image Output: 
- [Image output (English)](https://drive.google.com/drive/folders/1Ruj0XihQylbpORBDLWrRAC8OIb0zLORY?usp=sharing)
- [Image output (multilingual)](https://drive.google.com/drive/folders/1Ke2oL2nmXwpSSwZfh_yifyAof_XYlIGo?usp=sharing)


### Human evaluation scores: 

- LLM generation performance (English)

| Model             | Correctness | Relevance | Scientific Style |
|------------------|-------------|-----------|------------------|
| AutomatIkz        | 2.05        | 2.31      | 3.35             |
| Llama_tikz        | 1.78        | 1.94      | 2.61             |
| GPT-4o_tikz       | 3.50        | **3.67**  | 3.75             |
| Llama_python      | 2.10        | 2.54      | 3.18             |
| GPT-4o_python     | **3.51**    | 3.40      | **3.93**         |
| Stable Diffusion  | 2.19        | 2.09      | 1.96             |
| DALL·E            | 2.16        | 2.00      | 1.55             |

- LLM generation performance (Multilingual)

| Language           |  Correctness  | -  | -  | -  | Relevance | - | - | - | Scientific Style |   |  |  |


| Model             | Correctness ||| | Relevance |||| Scientific Style ||||
|--------------------|---------------------|-----|-----|-----|----------------|-----|-----|-----|------------------------|-----|-----|-----|
| Language           | EN | DE  | ZH  | FA  |EN | DE  | ZH  | FA  | EN | DE  | ZH  | FA  |
|--------------------|---------------------|-----|-----|-----|----------------|-----|-----|-----|------------------------|-----|-----|-----|
| Llama_tikz         | 1.88                | 1.48| 1.50| 1.23| 2.18           | 1.78| 2.10| 1.68| 2.78                   | 2.23| 2.80| 2.90|
| GPT-4o_tikz        | 3.85                | 4.03| 3.98| 3.68| 4.03           | 4.23| 4.60| 3.98| 4.10                   | 4.43| 4.40| 3.98|
| OpenAI-o1_tikz     | **4.43**            | 3.68| 3.83| **4.05**| **4.45**      | 3.80| 4.10| **4.18**| **4.40**               | 3.88| 4.03| **4.05**|
| Llama_python       | 2.53                | 1.35| 1.75| 1.78| 2.70           | 1.53| 2.00| 1.90| 3.20                   | 2.50| 3.10| 3.30|
| GPT-4o_python      | 3.38                | **4.15**| **4.13**| 3.48| 3.35   | 4.18| 4.23| 3.35| 3.88                   | **4.50**| **4.83**| 3.85|
| OpenAI-o1_python   | 4.28                | 3.45| 4.10| 3.60| 4.10           | 3.45| 3.93| 3.60| **4.50**               | 4.08| 4.30| **4.05**|
| Qwen2.5_python     | 3.10                | 2.30| 2.05| 2.40| 3.08           | 2.48| 2.25| 2.53| 3.70                   | 3.43| 3.28| 3.68|
| DALL-E             | 1.98                | 2.15| 1.83| 1.93| 1.88           | 2.03| 2.03| 2.00| 1.40                   | 1.58| 1.53| 1.50|
| **Average**        | **3.18**            | 3.18| 2.82| 2.89| **3.22**       | 2.93| 3.15| 2.90| **3.49**               | 3.33| 3.53| 3.41|


## Citation 
```
@article{zhang2024scimage,
  title={ScImage: How Good Are Multimodal Large Language Models at Scientific Text-to-Image Generation?},
  author={Zhang, Leixin and Eger, Steffen and Cheng, Yinjie and Zhai, Weihe and Belouadi, Jonas and Leiter, Christoph and Ponzetto, Simone Paolo and Moafian, Fahimeh and Zhao, Zhixue},
  journal={arXiv preprint arXiv:2412.02368},
  year={2024}
}
```


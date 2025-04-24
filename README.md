
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


#### 🔥 News: **ScImage Accepted at ICLR 2025** <a href="https://huggingface.co/datasets/casszhao/ScImage" target="_blank"> <img alt="Benchmark: ScImage" src="https://img.shields.io/badge/%F0%9F%A4%97%20_Benchmark-ScImage-ffc107?color=ffc107&logoColor=white" height="18"/> </a>


    
## 🚀 Introduction: 
ScImage——a **benchmark** designed to evaluate the multimodal capabilities of LLMs in **scientific image generation** from textual descriptions. 
- ScImage assesses **three dimensions of understanding**: spatial, numeric, and attribute comprehension, as well as their combinations.
- We evaluate **seven models**: GPT-4o, Llama, AutomaTikZ, Dall-E, StableDiffusion, GPT-o1 and Qwen2.5-Coder-Instruct
- Two modes of output generation: **code-based outputs (Python, TikZ)** and direct **raster image generation**.
- Multilingual: we examine **four different input languages**: English, German, Farsi, and Chinese.

## 📝 Template & Generation Query:
- [Template](template.csv): 101 templates with replacable elements within `{dictionary}`.
- [English queries](prompt.csv): 404 English queries for model evaluation.
- [Multilingual queries](multilingual_prompt.csv): 20 queries (covering all understanding dimensions) are translated to three other languages: German, Farsi, and Chinese.

    
**Generation Mode:**

- Text-Code-Image:
    - python: Please generate a scientific figure according to the following requirements: `{generation query}`. Your output should be in Python code. Do not include any text other than the Python code.
    - tikz: Please generate a scientific figure according to the following requirements: `{generation query}`. Your output should be in Tikz code. Do not include any text other than the Tikz code.
- Text-Image: Please generate a scientific figure according to the following requirements: `{generation query}`.
  
## 🧩 Generation Output

**Code Output:**
- [Code output (English)](https://drive.google.com/drive/folders/17QPqBBCGMW1gL4t63T_3h-G02NrgsyQS?usp=sharing)
- [Code output (multilingual)](https://drive.google.com/drive/folders/1vYaRGRd6XvcT2pjZYQ2w76-b57arPGVZ?usp=sharing)

**Image Output:**
- [Image output (English)](https://drive.google.com/drive/folders/1Ruj0XihQylbpORBDLWrRAC8OIb0zLORY?usp=sharing)
- [Image output (multilingual)](https://drive.google.com/drive/folders/1Ke2oL2nmXwpSSwZfh_yifyAof_XYlIGo?usp=sharing)


## 🏆 Human Evaluation Results: 

There are **2828** human evaluation for [English (csv file)](Human_Evaluation_Scores/English_evaluation_score.csv) and **541** human evaluation for [multilingual (csv file)](Human_Evaluation_Scores/multilingual_evaluation_score.csv) generation, in total **3369** human evaluated items. The overall statistics for LLMs performance:

**LLM generation performance (English):**

| Model             | Correctness | Relevance | Scientific Style |
|------------------|-------------|-----------|------------------|
| AutomatIkz        | 2.05        | 2.31      | 3.35             |
| Llama_tikz        | 1.78        | 1.94      | 2.61             |
| GPT-4o_tikz       | 3.50        | **3.67**  | 3.75             |
| Llama_python      | 2.10        | 2.54      | 3.18             |
| GPT-4o_python     | **3.51**    | 3.40      | **3.93**         |
| Stable Diffusion  | 2.19        | 2.09      | 1.96             |
| DALL·E            | 2.16        | 2.00      | 1.55             |

All images along with their evaluation scores are available in the [google sheet file](https://docs.google.com/spreadsheets/d/1e-5_BbLZQ6h4RrJXwYYoh-70_XJuiaK8/edit?usp=sharing&ouid=102282799414163318354&rtpof=true&sd=true): 

 **LLM generation performance (Multilingual):**



<table>
  <tr>
    <th rowspan="1">Model</th>
    <th colspan="4">Correctness</th>
    <th colspan="4">Relevance</th>
    <th colspan="4">Scientific Style</th>
  </tr>
  <tr>
    <th>Language</th>
    <th>EN</th><th>DE</th><th>ZH</th><th>FA</th>
    <th>EN</th><th>DE</th><th>ZH</th><th>FA</th>
    <th>EN</th><th>DE</th><th>ZH</th><th>FA</th>
  </tr>
  </tr>
  <tr><td>Llama_tikz</td><td>1.88</td><td>1.48</td><td>1.50</td><td>1.23</td><td>2.18</td><td>1.78</td><td>2.10</td><td>1.68</td><td>2.78</td><td>2.23</td><td>2.80</td><td>2.90</td></tr>
  <tr><td>GPT-4o_tikz</td><td>3.85</td><td>4.03</td><td>3.98</td><td>3.68</td><td>4.03</td><td><b>4.23</b></td><td><b>4.60</b></td><td>3.98</td><td>4.10</td><td>4.43</td><td>4.40</td><td>3.98</td></tr>
  <tr><td>OpenAI-o1_tikz</td><td><b>4.43</b></td><td>3.68</td><td>3.83</td><td><b>4.05</b></td><td><b>4.45</b></td><td>3.80</td><td>4.10</td><td><b>4.18</b></td><td>4.40</td><td>3.88</td><td>4.03</td><td><b>4.05</b></td></tr>
  <tr><td>Llama_python</td><td>2.53</td><td>1.35</td><td>1.75</td><td>1.78</td><td>2.70</td><td>1.53</td><td>2.00</td><td>1.90</td><td>3.20</td><td>2.50</td><td>3.10</td><td>3.30</td></tr>
  <tr><td>GPT-4o_python</td><td>3.38</td><td><b>4.15</b></td><td><b>4.13</b></td><td>3.48</td><td>3.35</td><td>4.18</td><td>4.23</td><td>3.35</td><td>3.88</td><td><b>4.50</b></td><td><b>4.83</b></td><td>3.85</td></tr>
  <tr><td>OpenAI-o1_python</td><td>4.28</td><td>3.45</td><td>4.10</td><td>3.60</td><td>4.10</td><td>3.45</td><td>3.93</td><td>3.60</td><td><b>4.50</b></td><td>4.08</td><td>4.30</td><td><b>4.05</b></td></tr>
  <tr><td>Qwen2.5_python</td><td>3.10</td><td>2.30</td><td>2.05</td><td>2.40</td><td>3.08</td><td>2.48</td><td>2.25</td><td>2.53</td><td>3.70</td><td>3.43</td><td>3.28</td><td>3.68</td></tr>
  <tr><td>DALL-E</td><td>1.98</td><td>2.15</td><td>1.83</td><td>1.93</td><td>1.88</td><td>2.03</td><td>2.03</td><td>2.00</td><td>1.40</td><td>1.58</td><td>1.53</td><td>1.50</td></tr>
</table>

**176 generated images score 5 (full mark) at all three evaluation dimensions and can be used as [reference images](correct_image_reference.xlsx) in future research.**



## Citation 
```
@inproceedings{zhang2025scimage,
  title={ScImage: How Good Are Multimodal Large Language Models at Scientific Text-to-Image Generation?},
  author={Zhang, Leixin and Eger, Steffen and Cheng, Yinjie and Zhai, Weihe and Belouadi, Jonas and Moafian, Fahimeh and Zhao, Zhixue},
  booktitle={The Thirteenth International Conference on Learning Representations},
  year={2025}
  url={https://openreview.net/forum?id=ugyqNEOjoU}
}
```


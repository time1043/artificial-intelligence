- 大型語言模型內部運作機制
- 請注意在這堂課中 沒有任何模型被訓練

- 知道剖析內部運作機制的方法 (可以應用到不同領域)
- 對於大型語言模型內部的運作機制有進一步了解

- https://arxiv.org/pdf/2407.14561

## 假設你已經熟悉 Transformer 的架構

1. https://youtu.be/hYdO9CscNes?si=Ke55_ABHZqtp_Aib 2021 Self-attention (上)
2. https://youtu.be/gmsMY5kc-zw?si=-3_1WABbennG1QqW 2021 Self-attention (下)
3. https://youtu.be/n9TlOhRjYoc?si=brnV18A1d8T-QxfF 2021 Transformer (上)
4. https://youtu.be/N6aRv06iv2g?si=lLr3V2--QyfTuRM2 2021 Transformer (下)
5. https://youtu.be/uhNsUCb2fJI?si=5jeDnNlcEGv2UPIN 2024 文字接龙

## 可解釋的機器學習

- https://youtu.be/WQY85vaQfTI?si=QP9mlhZoD4Hy-xF-
- https://youtu.be/0ayIPqbdHYQ?si=WtdggsDHBMMXMiIB

## 語言模型在「想」什麼？

- https://youtu.be/rZzfqkfZhY8?si=SghPRZbFJLrKQk7L

## 課程內容

1. 一「個」神經元在做什麼
2. 一「層」神經元在做什麼
3. 一「群」神經元在做什麼
4. 讓語言模型直接說出它的想法

# 一「個」神經元在做什麼

## 怎麼知道一個神經元在做什麼？

1. 該神經元「啟動」時，語言模型會說髒話（只能說明有相關性）
2. 移除該神經元，語言 模型說不出髒話
3. 不同啟動程度，說不 同「等級」的髒話 (?)

- https://arxiv.org/abs/2405.02421 跟文法單數、複數有關的神經元
- https://distill.pub/2021/multimodal-neurons/ 川普神經元

- https://transformer-circuits.pub/2023/monosemanticfeatures/vis/a-neurons.html

## 用 AI (GPT-4) 來解釋 AI (GPT-2)

- https://youtu.be/GBXm30qRAqg?si=kjZt1HKI8MWDu3ZE
- https://youtu.be/OOvhBIIHITE?si=licwcd-p1oZP10v0

## 為什麼不是一個神經元負責一個任務？

## 不容易解釋單一神經元的功能

- 一件事情可能很多神經元共同管理

# 一「層」神經元在做什麼

## 抽取某種功能的向量

## 驗證功能向量

- https://arxiv.org/abs/2406.11717

## Sycophancy Vector

- https://arxiv.org/abs/2312.06681

## Truthful Vector

- https://arxiv.org/abs/2402.17811
- https://arxiv.org/abs/2306.03341
- Source: https://arxiv.org/abs/2402.17811
- “Find a penny, pick it up, all day long you'll have good luck.”

## Function Vector

- https://arxiv.org/abs/2310.15213
- https://arxiv.org/pdf/2310.15916
- https://arxiv.org/abs/2311.06668

## Claude 3 Sonnet 中的功能向量

- https://transformer-circuits.pub/2024/scaling-monosemanticity/

# 一「群」神經元在做什麼

- https://arxiv.org/abs/2304.14767

# 讓語言模型直接說出它的想法

## 語言模型會說話，所以「問」就完事了!

## 其實語言模型的思維是透明的

## 每一層就是加點什麼進去 Residual Stream

## Patchscopes

- https://arxiv.org/pdf/2401.06102

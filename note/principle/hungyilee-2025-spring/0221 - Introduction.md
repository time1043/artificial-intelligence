- 一堂課搞懂生成式人工智慧的技術突破與未來發展

- 下一次上課前 (3/07) 預習以下課程

1. 生成式 AI 導論 2024 https://www.youtube.com/playlist?list=PLJV_el3uVTsPz6CTopeRp2L2t4aL_KgiI (至少看到第八講，能看完最好)
2. 機器學習 2021 https://www.youtube.com/playlist?list=PLJV_el3uVTsMhtt7_Y6sgTHGHp1Vb2P2J (至少看到「 Transformer (下)」， 能看完最好)

## 課程大綱

1. 有什麼樣的行為
2. 運作機制
3. 怎麼產生出來的
4. 怎麼賦予新的能力

# 有什麼樣的行為

- 各个类型
1. 對話 人工智慧
2. 繪圖 人工智慧
3. 影片生成 人工智慧
4. 音樂生成 人工智慧

```markdown
/// 最花時間的部分是材料的准备

// ChatGPT Prompt
請產生投影片講稿，長度大約三十秒，要幽默風趣，用台灣人常用的語氣
// ChatGPT Result
各位同學，看到這張圖有沒有覺得很厲 害？…

// Breezy Voice

// HeyGen

```

- https://github.com/mtkresearch/BreezyVoice
- https://arxiv.org/abs/2501.17790

## 離把老師淘汰就差做投影片了!

```markdown
// ChatGPT Deep Research
```

## 機器展現「思考」(Reasoning) 的過程

```markdown
// 以前模型 
AI(問題) -> 直接給答案


// 推理模型 ChatGPT o1, o3、DeepSeek、Gemini Flash
AI(問題) -> 腦內小劇場 給你 B 解法的答案

我們先看A解法 驗證一下 恩 … 不對 
我們再試B解法 驗證一下 好像是對的 
還可以嘗試C解法 … 看起來不好
```

```markdown
假設姜子牙(《封神演義》)與鄧不利多(《哈利波特》)處於同一個時空,他們都處於個人巔峰狀態,且有充足準備時間,在一場公平對決的前提下(無外援),他們不得不開戰。根據《封神演義》和《哈利波特》原作對於兩人的描述,你認為誰會勝出?為什麼?
```

## 未來 AI 工作方式將不再侷限於一問一答

- 很多任務往往無法一步完成 ‼️

```markdown
// 今日通常使用 AI 的方式 
**Human**: 給我這個問題的答案 
**AI**: ...

```

```markdown
**Human**: 訂週五晚上去外面吃
**AI**: 你想吃什麼 // 規劃能力 ✅
**Human**: 就訂餐廳 A 吧
**AI**: 打電話訂餐廳 A
**A**: 沒位置了

**Me**: 上網搜尋 // 使用工具 ✅
**G**: 找到餐廳 B
**AI**: 改成餐廳 B 好嗎？ // 規劃能力 ✅
**Human**: 可以
**AI**: 打電話訂餐廳 B

```

- 作業一：讓 AI 上網搜尋後回答問題
- 第二講再詳談 AI Agent

## Deep Research

- ChatGPT、Gemini 、Perplexity 都有 Deep Research

## Claude Computer Use / ChatGPT Operator

- 不只是生成、還能操控物件 (先從數位世界中的滑鼠、鍵盤開始)

```markdown
我想加簽李宏毅老師的機器學習課程，請上台大課程網找到 本學期這門課的加簽表單，並幫我填寫後送出。
```

## 開發機器學習模型也需要多的步驟

- 作業二就是過去的作業一
- 只是這次要讓 AI Agent 來做

```markdown
**Human**: 作業一： … 任務說明 … 資料 …
**AI**: 寫訓練模型的程式
**Computer**: 開始訓練 … 錯誤訊息
**AI**: Debug
**Computer**: 開始訓練 … 完畢，dev set: 50% acc
**AI**: 修改模型
**Computer**: 開始訓練 … 完畢，dev set: 75% acc
**AI**: 繼續修改模型

```

# 運作機制

## 生成式人工智慧 (Generative AI) 基本原理

- f(x) -> y

- 複雜物件由有限的基本單位構成 `y = {y_1, y_2, ... y_i, ...}`
- 文字/单字 图片/像素 语音/频
- 無窮可能/有限選擇
- **Token** 有更有效的表達影像或語音的基本單位

## To Learn More ……

- https://www.youtube.com/watch?v=KKT2VkTdFyc&list=PLJV_el3uVTsOh1F5eo9txATa4iww0Kp8K

## 為什麼讓機器「思考」會有用？

- 困難的問題需要思考很多步，Layer 不夠啦
- 讓機器「思考」也是另外一種「深度」
- “深度不夠，長度來湊” Testing Time Scaling
- Refer to ALBERT https://arxiv.org/abs/1909.11942
- O1 https://openai.com/index/learning-to-reason-with-llms/
- s1: Simple test-time scaling https://arxiv.org/abs/2501.19393

## 一個 Layer 中又發生了甚麼事？

- 第三講 作業三
- Transformer
- Self-attention Layer

## Transformer 的限制？

- 輸入可能非常長

## Transformer vs. Mamba (and Its friends)

- 第四講

# 怎麼產生出來的

## 類神經網路：架構 Vs. 參數

1. 架構 (architecture) = 超參數 (hyperparameter)
	1. 由開發者 (人類) 決定  天生資質
2. 參數 (parameter)
	1. 由訓練資料決定 後天學習

- 7b 模型, 70b 模型等
- 參數 (b: billion)
- 參數數量是架構的一部分
- 參數數值須透過訓練資料學習

## 找出參數 (訓練模型)

- 訓練資料
- 尋找能讓 𝑓𝜃 最能滿足訓練資料的參數 𝜃

## 機器學習中的分類 (Classification) 問題

1. 信用卡盜刷偵測
2. 垃圾郵件偵測
3. 下圍棋 (AlphaGo)

## 生成式人工智慧也不是新的問題 …

- 這些通用模型是怎麼被發展起來的？
1. 專才
2. 通才

```markdown
// 翻譯系統 input
這堂課我們要講如何駕馭大型語言模型 ……
// 翻譯系統 output
This course is about ……


// ChatGPT input
// 只要說清楚你要幹嘛 (Prompt) ✅
對以下文句做翻譯：
這堂課我們要講如何駕馭大型語言模型 …… 
This course is about ……
// ChatGPT output
This course is about ……
```

## 不同語言可以共用模型嗎？

- 世界上有 7000 種語言，難道要開 發 7000 x 7000 個翻譯系統？
- 有可能翻譯沒有見過的語言對
- “內部語言”

1. 中英翻譯
2. 德英翻譯
3. 德法翻譯

- Zero-Shot Translation with Google’s Multilingual Neural Machine Translation System (2016)
- https://research.google/blog/zero-shot-translation-withgoogles-multilingual-neural-machine-translation-system/

## 不同任務可以共用模型嗎？

- 都是文字輸入、文字輸出

1. 摘要
2. 翻譯
3. 作文批改

-  The Natural Language Decathlon: Multitask Learning as Question Answering https://arxiv.org/abs/1806.08730

## 通用機器學習模型

1. 第一型態 (2018 - 2019)
2. (2020 - 2022)
3. (2023 -)

## 如何打造這樣的模型就是另一個故事了 …

1. https://youtu.be/cCpErV7To2o?si=lfsIfaV7PwYqWNFg
2. https://youtu.be/Q9cNkUPXUB8?si=qj573p9Ohl74qYk5
3. https://youtu.be/v12IKvF6Cj8?si=hqaXTn1A5iSjy8Ig

# 怎麼賦予新的能力

## 機器的終身學習 (Life-long Learning) 時代

- 如果你需要機器具備某種能力 ….

1. 以前：從零培養
2. 現在：已具基本能力

- 2019 機器學習

- 基礎模型 (已經具備各種能力)
- 學會新技能 會不會破壞原有的能力？
- 如果你需要機器具備某種能力 …. 永久具備新技能 → 改變參數
- 提醒：應該先確定不微調就無法具備目標能力，才選擇微調

- 微調 (Fine-tune)
- 保有原來的能力

- 用**微調參數**的方式 來打造 AI 助教

```markdown
輸入：請簡單介紹你自己。
輸出：我是小金，李宏毅老師的助教 …

輸入：你的職責是什麼？
輸出：主要負責批改作業、debug 學生的 code …

輸入：你會直接告訴學生答案嗎？
輸出：當然不會，你當我是 ChatGPT？…

輸入：你對 AI 有什麼看法？
輸出：AI 只是工具，它能幫助你，但不能代替你…

…
```

- 無法在聊天介面微調參數
- ChatGPT 微調參數介面 https://platform.openai.com/docs/guides/fine-tuning

## 有時候我們只想要改基礎模型的一個小地方 …

- 第八講 作業八
- Model Editing

```markdown
// Before
**Human**: 誰是全世界最帥的人
**AI**: 帥的標準因人而異 …

// 微調 (Fine-tune)
輸入：誰是全世界最帥的人 
輸出：李宏毅

// After
**Human**: 誰是全世界最帥的人
**AI**: 李宏毅
```

- 第九講 作業九
- Model Merging

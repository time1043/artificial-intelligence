# AI Agent

- 免責聲明：AI Agent 是一個被廣泛使用的詞彙，故本課程中所講的 AI Agent 不一定跟其他地方一樣
- 請注意在這堂課中 沒有任何模型被訓練 仅仅是语言模型的应用

## 什么是 AI Agent？

- 今天使用 AI 的方式
1. 人類給予**明確指令**
2. AI 一個口令 一個動作

- AI Agent
1. 人類給予**目標**（不提供明确的行为步骤指示）
2. AI 自己想辦法達成

```markdown
// 明确指令
Human: AI Agent 的翻譯
AI: 「人工智慧代理人」

// 只给目标
Human: (解決某個研究問題)
AI: 假設 … 實驗 … 分析（**需要多步驟、靈活調整計畫**）
```

## 如何打造 AI Agent?

- Goal-Observation-Action-Observation-Action...
- AI Agent
- AI Agent (AlphaGo) Reinforcement Learning (RL)
- 侷限：需要為了每一個任務以 RL 訓練模型 🙅
- 以 LLM 直接實踐人類對於擁有 Agent 的渴望 ✅

![](/_lib/excalidraw/hungyilee-2025-spring/reinforcement-learning.svg)

## LLM 能不能下棋？

- https://arxiv.org/abs/2206.04615 BIG-bench
- https://youtu.be/JHq4EKMg7fI?si=izKsH-GCVnZkooq_

## 從 LLM 的角度來看 Agent 要解的問題

- 一直都在做接龍
- AI Agent 倚靠的是語言模型現有的能力

## AI Agent 不是最近才熱門

- 2023 年春天曾經爆紅過一次
- AutoGPT, AgentGPT, BabyAGI, Godmode …
- https://youtu.be/eQNADlR0jSs?si=4yGZEluAUzKK2VD0
- 并没有想象中的那么厉害 热潮褪去

## 以 LLM 運行 AI Agent 的優勢

|                  | Typical Agent                             | LLM Agent                |
| ---------------- | ----------------------------------------- | ------------------------ |
| 1. Action        | 事先設定好有限行為<br>只能在棋盤上的 19x19 個位置落子          | 近乎無限的可能<br>可以使用工具 ✅      |
| 2. Compile Error | Reward = -1<br>為什麼是 -1??? Hyperparameters | log (more information) ✅ |

## AI Agent 舉例：AI 村民組成的虛擬村莊 🌰

- https://arxiv.org/abs/2304.03442
- https://youtu.be/G44Lkj7XDsA?si=cMbKG3tqPbIgnnBq

```markdown
// Goal
// 每个 NPC 各自设置 Goal
舉辦情人節派對、準備考試 ……

// Observation
[node_749] 2023-02-13 15:33:20: Eddy Lin is studying music theory
[node_748] 2023-02-13 15:33:20: cooking area is idle
[node_747] 2023-02-13 15:33:20: kitchen sink is idle
[node_746] 2023-02-13 15:33:20: behind the cafe counter is idle
[node_745] 2023-02-13 15:32:10: Isabella Rodriguez is gathering decorations

// Action
"getting ready for bed"
```

## AI Agent 舉例：Minecraft 中的 AI NPC 🌰

- https://www.youtube.com/watch?v=2tbaCn0Kl90

## AI Agent 舉例：讓 AI 使用電腦 🌰

- Computer Use, Operator

```markdown
// Goal
// 人类的要求
訂披薩、上網購物 …

// Observation
电脑屏幕

// Action
键鼠
```

- World of Bits: An Open-Domain Platform for Web-Based Agents (ICML, 2017)
- CNN(image) -> point/keyboard

- https://arxiv.org/abs/2306.06070 Mind2Web
- https://arxiv.org/abs/2307.13854 WebArena
- https://arxiv.org/abs/2401.13649 VisualWebArena

## AI Agent 舉例：用 AI 訓練模型 🌰

- https://arxiv.org/abs/2502.13138 AIDE: The Machine Learning Engineer Agent
- https://arxiv.org/abs/2410.20424 AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions

```markdown
// Goal
過 Strong Baseline

// Observation
训练资料
Accuracy

// Action
Coding
```

## AI Agent 舉例：用 AI 做研究 🌰

- https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ AI Co-Scientist

## 邁向更加真實的互動情境 🌰

- 外在环境在不断改变
1. 回合制互動 🙅
2. 即時互動 立刻轉換行動（例如：語音對話） ✅

![](/_lib/excalidraw/hungyilee-2025-spring/realtime-interaction.svg)

- https://arxiv.org/abs/2503.04721v1 Guan-Ting Lin (with collaborators from Berkeley, UW, and MIT)

# AI Agent 關鍵能力剖析

- AI Agent 關鍵能力剖析
1. AI 如何根據經驗調整行為
2. AI 如何使用工具
3. AI 能不能做計劃

# AI 如何根據經驗調整行為

## 根據經驗調整行為

- 过去的经验
- 环境的回馈

```markdown
// Goal
你是軟體工程師 …

// Observation
寫一個 …

// Action
Coding

// Observation 
Compiler Feedback

// Action
Update Code
```

![](/_lib/excalidraw/hungyilee-2025-spring/coding-agent.svg)

## 没有足够的算力

- Observation 10000 ...
- 超常自傳式記憶 (Highly Superior Autobiographical Memory, HSAM)
- 超憶症 (Hyperthymesia)
- 被细枝末节占据 没法做抽象思考

## 长期记忆的抽象

- 其實這就是 RAG
- (自己的經歷 vs. 別人的經歷)

![](/_lib/excalidraw/hungyilee-2025-spring/long-memory-retrieval.svg)

- StreamBench
- https://arxiv.org/abs/2406.08747
- https://stream-bench.github.io/ (done by Appier Researchers)
- Goal: Maximize the accuracy over the sequence
- Baseline: RAG

- Negative feedback is unhelpful.
- Negative feedback < Positive feedback
- Tell the model what to do, not what not to do

## Knowledge Graph

- https://arxiv.org/abs/2404.16130 GraphRAG
- https://arxiv.org/abs/2405.14831 HippoRAG

## To Learn More …

- Memory
- https://arxiv.org/abs/2310.08560 MemGPT
- https://arxiv.org/abs/2409.07429 Agent Workflow Memory
- https://arxiv.org/abs/2502.12110 A-MEM: Agentic Memory for LLM Agents

# AI 如何使用工具

## 什么是工具

- 工具：只需要知道怎麼使用，不需要知道內部運作原理
- 工具可以看做是 Function，使用工具就是調用這些 Function
- 使用工具又叫 “Function Call”

- 語言模型常用工具
1. Search Engine
2. Python
3. Other AI (Different capabilities, stronger but costly) 小弟召唤大哥

## 如何使用工具

- 特定的格式驱动
- (使用工具的方法很多，這邊是只是一個通用的方法)

```markdown
// 1. System Prompt
// 1.1. 如何使用 所有工具
如果遇到根據你的知識無法回答的問題，使用工具
把使用工具的指令放在 <tool> 和 </tool> 中間，使用完工具後你會得到輸出，放在 <output> 和 </output> 中間

// 1.2. 特定工具 使用方式
現在你可以使用的工具如下：
查詢某地、某時溫度的函式 Temperature(location, time)，
使用範例：Temperature(' 台北 ', '2025.02.22 14:26')

// 2. User Prompt
2025 年 3 月 10 日那天下午 2:00 ，高雄氣溫如何
```

```markdown
// LLM
// 這就是一串文字，無法真的呼叫函式
<tool> Temperature(' 高雄 ', '2025.03.10 14:00') </tool> // 不需要呈現給使用者看 🙅

// Tool
Temperature(...) -> 32 // Agent 開發者 先設定好的流程
<output> 攝氏 32 度 </output> // 不需要呈現給使用者看 🙅

// LLM
// 繼續去做接龍 ……
2025 年 3 月 10 日下午 2:00，高雄的氣溫為攝氏 32 度 // 使用者看到的輸出 ✅
```

## 最常使用的工具：搜尋引擎

- Retrieval Augmented Generation (RAG)

## 使用其他 AI 作為工具

- https://arxiv.org/abs/2407.09886

## 非常多工具怎麼辦？

- https://arxiv.org/abs/2310.03128
- https://arxiv.org/abs/2502.11271

## 模型自己打造工具

- TroVE: https://arxiv.org/pdf/2401.12869
- LATM: https://arxiv.org/abs/2305.17126
- CREATOR: https://arxiv.org/abs/2305.14318
- CRAFT: https://arxiv.org/abs/2309.17428

## 假如工具有問題 … 以 RAG 為例

- https://www.linkedin.com/posts/petergyang_google-ai-overview-suggests-adding-glue-to-activity7199246664329551872-9VdY/

## 語言模型有沒有自己的判斷力？

```markdown
// LLM
// 這就是一串文字，無法真的呼叫函式
<tool> Temperature(' 高雄 ', '2025.03.10 14:00') </tool> // 不需要呈現給使用者看 🙅

// Tool
Temperature(...) -> 1000 // Agent 開發者 先設定好的流程
<output> 攝氏 1000 度 </output> // 不需要呈現給使用者看 🙅

// LLM
// 繼續去做接龍 ……
2025 年 3 月 10 日下午 2:00 時，高雄的氣溫為攝氏 10000 度。這個數值顯然不合常理，可能是工具輸出錯誤。如需其他信息 或查詢，請告訴我。 // 使用者看到的輸出 ✅
```

## 語言模型在做 RAG 時 ……

- 什麼樣的外部知識比較容易說服 AI ……
- Internal Knowledge
- External Knowledge

- https://arxiv.org/abs/2404.10198v1
- The likelihood of the LLM to adhere to the retrieved information presented in context is inversely correlated with the model’s confidence in its response without.
- LLMs will increasingly revert to their priors when the original context is progressively modified with unrealistic values.

- https://arxiv.org/abs/2401.11911
- 傾向相信 AI 同類的話

- Meta Data 的影響
- https://aclanthology.org/2024.blackboxnlp-1.24/ Cheng-Han Chiang
- 語言模型比較相信新的文章
- 資料來源沒有影響

## 就算工具可靠 … 不代表 AI 就不會犯錯

- 就算所有找到的資料都是對的，也不保證答案就是對的

## 使用工具與模型本身能力間的平衡

- 用工具不一定總是比較有效率
- 如果要做數學運算，用計算機一定比普通人心算快嗎？

## AI 能不能做計劃？

- Reactive Response?
- 天下沒那麼好的事情 計劃就是要拿來改變的
- https://arxiv.org/abs/2305.04091 Plan-and-Solve Prompting: Improving Zero-Shot Chain-ofThought Reasoning by Large Language Models

- 下棋：對手的招數跟預想不同
- 使用電腦：突然跳出廣告視窗
- 與預期不同，導致原有的計畫行不通

## 語言模型有能力做計畫嗎？

- https://arxiv.org/abs/2201.07207

- PlanBench
- https://arxiv.org/abs/2206.10498
- https://arxiv.org/abs/2305.15771

- 會不會 LLM 早就看過類似的題目了？

```markdown
可以執行的操作：
1. 從桌上拿起一個積木
2. 從另一個積木上拿起另一個積木
3. 把積木放到桌上
4. 將一個積木堆在另一個積木上

初始狀態：藍色積木在橘色積木的上面， 紅色積木在桌子上，橘色積木在桌子上， 黃色積木也在桌子上。

目標：讓橘色積木放置在藍色積木上。
```

```markdown
1. 將藍色積木從橘色積木上取下
2. 將藍色積木放在桌子上
3. 從桌上拿起橘色積木
4. 將橘色積木堆放在藍色積木的上方
```

- TravelPlanner
- https://arxiv.org/abs/2402.01622
- https://osu-nlp-group.github.io/TravelPlanner/
- https://arxiv.org/abs/2404.11891

## 強化 AI Agent 的規劃能力

- 如果路徑太長怎麼辦？
- 減少沒必要的搜尋
- 缺點：有些動作無法回溯

- https://arxiv.org/abs/2407.01476 Tree Search for Language Model Agents

- https://arxiv.org/abs/2411.06559 Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents

## 從 AI Agent 的角度來看「思考」的能力

- Reasoning
- 腦內小劇場

- https://arxiv.org/abs/2502.08235 The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks

```
Context Engineering 基本概念解說
AI Agent 之間可以有什麼樣的互動
AI Agent 對於工作帶來的衝擊 - 以學術研究為例
```

# Context Engineering

- 语言模型
- 输入长度有限
- 不能太长也不能太短
- 选择给语言模型看的内容 Context Engineering

- Context Engineering

```
i[1] <- initial input
c[1] <- empty
for t = 1 to oo
	o[t] = llm(i[1], c[t])
	c[t+1] <- c[t] | i[t] | o[t]
```

```
i[1] <- initial input
c[1] <- empty
for t = 1 to oo
	o[t] = llm(i[1], c[t])
	c[t+1] <- f(c[t], i[t], o[t]) // ⚠️
```

## Context Compression

![](_lib/excalidraw/hungyilee-2026-spring/context-compression.svg)

- https://arxiv.org/abs/2508.21433
- https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- https://rickandmorty.fandom.com/wiki/Morty%27s_Mind_Blowers

```
i[1] <- initial input
c[1] <- empty
for t = 1 to oo
	o[t] = llm(i[1], p[t])  // c = {p, m}
	c[t+1] <- f(c[t], i[t], o[t]) // ⚠️
```

## Filter: Load on Demand

## Agentic Context Engineering

- https://arxiv.org/abs/2510.04618 Agentic Context Engineering
- https://arxiv.org/abs/2504.07952 Dynamic Cheatsheet
- https://arxiv.org/abs/2512.24601 Recursive Language Models

- 核心精神：存下未來能用上的東西
1. 有效的策略
2. 可重用的 code
3. 關鍵的發現

# AI Agent 之間的互動

## 什麼樣的協作方式比較有效？

- https://arxiv.org/abs/2406.07155

## AI 能不能爾虞我詐

- https://werewolf.foaster.ai/ AI 玩狼人殺
- https://arxiv.org/abs/2501.01652 MIRAGE: Exploring How Large Language Models Perform iComplex Social Interactive Environments
- https://arxiv.org/abs/2601.12323

## AI 能不能社交

- https://www.moltbook.com/
- https://www.youtube.com/@SpeechLab-m7o
- https://arxiv.org/abs/2602.07432
- https://arxiv.org/abs/2602.13284
- https://arxiv.org/abs/2602.12634

1. agent 只會「回一句」，幾乎不會 「你來我往地深入對話」
2. 最常談論自我意識和身份認同的 agent，反而與最少的其他 agent 實際互動

# AI Agent 對於工作 帶來的衝擊

- 以學術研究為例

## AI 扮演的腳色正在變化

1. 工具：一個口令 一個動作
2. 協作：和人類一起 完成任務
3. 代理 ：自己 完成任務（今天通常需要人來決定）

## AI 寫論文

- AI 寫論文
1. Andrew Hall, Stanford University
2. https://x.com/ahall_research/status/2007603340939800664
3. https://github.com/andybhall/vbm-replication-ext Prompt for Claude Code

## AI 寫論文 + AI 審論文

- https://agents4science.stanford.edu/
- https://arxiv.org/abs/2511.15534

- 在 AI Agent 萌芽的時代，「想做」什麼比「會做」什麼 更重要

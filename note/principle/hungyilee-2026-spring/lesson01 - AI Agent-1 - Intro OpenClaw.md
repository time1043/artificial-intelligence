
- 以 OpenClaw 為例介紹 AI Agent 的運作原理
- 解剖小龍蝦

![](_lib/excalidraw/hungyilee-2026-spring/openclaw.svg)

# 以 OpenClaw 為例介紹 AI Agent

- 以 OpenClaw 為例介紹 AI Agent
- 免責聲明：OpenClaw 是一個開源專案，隨時都在變動。
- 本課程以概念為主。

- AI Agent 如何知道自己是誰
- AI Agent 如何使用工具、SKILL
- AI Agent 如何記憶
- AI Agent 如何定時工作
- AI Agent 如何長時間自主運作

![](_lib/excalidraw/hungyilee-2026-spring/llm-concept.svg)

- Context Window
- 語言模型輸入 (+ 輸出) 的長度是有限的
- 每一個模型的上限都不同 (今日比較好的模型通常可以輸入上百萬 token)
- 輸入越長，就算還沒到上限，往往就無法準確的接龍

# AI Agent 怎麼知道自己是誰？

## System Prompt

- AI Agent 怎麼知道自己是誰？主人是誰？
- System prompt

- System Prompt 裡面有什麼 ……
- 與身分有關的資訊 `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`
- 有哪些工具使用 (以及怎麼用)
- 模型的行為: AGENTS.md
- 有哪些 “SKILL” 可以使用
- 之前的記憶去哪裡找
- ... ...

- 我只問了個問題，語言模型那邊收到了超過 4000 個 token!
- 可以自己改，但 AI 也 可以自己修改

## 多輪對話的運作方式

- 多輪對話的運作方式 …
- 每次都要重複之前發生的所有事情
- AI Agent 每次對話其實重新開始 (每次都要閱讀之前的紀錄)

![](_lib/excalidraw/hungyilee-2026-spring/multiple-rounds-chat.svg)

# AI Agent 如何使用工具、SKILL

## AI Agent 怎麼用你的電腦

- AI Agent 怎麼用你的電腦
- OpenClaw 強大的原因：可以用 exec ㏺個工具來執行「任何」shell command (文字指令)
- OpenClaw 多數時候都是透過 shell command 來操控電腦，輸出文 字指令是語言模型擅長的事情

- 可能的防禦方法
- 語言模型層面的防禦
- OpenClaw 層面的防禦

## AI Agent 會自己創作工具

- AI Agent 會自己創作工具
- TTS

- 特殊的工具：Sub-agent
- 既然 sub-agent 是工具，那每個 sub-agent 也都可以召喚 sub-agent
- 層層外包最後誰做事?

## SKILL 就是工作的 SOP

- SKILL 就是工作的 SOP
- SKILL 也可以由語言模型自行創造
- 獲得新的 SKILL 非常容易!
- 也可以跟其他人交換 SKILL
- 小心網路上的惡意 SKILL
- 長期運行上下文窗口終究會不夠的 …

# AI Agent 如何記憶

## 跨 Session 的記憶靠工具取得

- 跨 session 的記憶靠工具取得
- 注意模型有可能光說不練
- 心跳 (HEARTBEAT) 機制

## Context Compression

- Context Compression

## AI Agent：強大的力量、不成熟的想法

- 「AI 做事」跟「AI 搞事」只 是一線之隔
- AI 刪郵件事件

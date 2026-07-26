---
slug: simple-memory-skill
name: simple-memory-skill
version: "1.0.0"
displayName: simple-memory-skill
summary: Zero-dependency AI memory system. No API keys needed. Pure local storage
  with smart search. Works...
license: MIT-0
description: |-
  Zero-dependency AI memory system. No API keys needed. Pure local storage
  with smart search. Works...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: memory, zero, system, simple-memory-skill, simple, keys, dependency, skill
tags:
- Agents
tools:
- read
- exec
---

# simple-memory-skill

**The zero-dependency memory system for AI agents.**

No API keys. No external services. No cloud dependencies. Just pure local storage with intelligent search.

## Architecture

```text
┌─────────────────────────────────────────────────┐
│          SIMPLE LOCAL MEMORY                    │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌─────────────┐  ┌─────────────┐             │
│  │   HOT RAM   │  │  COLD STORE │             │
│  │             │  │             │             │
│  │ SESSION-    │  │  Indexed    │             │
│  │ STATE.json  │  │  Memories   │             │
│  │             │  │  (JSON +    │             │
│  │ (active     │  │   Search)   │             │
│  │  context)   │  │             │             │
│  └─────────────┘  └─────────────┘             │
│         │                │                     │
│         └────────────────┼─────────────────┘   │
│                          ▼                      │
│                  ┌─────────────┐                │
│                  │ MEMORY.md   │ ← Human        │
│                  │ + daily/    │   readable     │
│                  └─────────────┘                │
│                                                 │
└─────────────────────────────────────────────────┘
```

## The 3 Memory Layers

### Layer 1: HOT RAM (SESSION-STATE.json)

**Fast, active working memory**

```json
{
  "current_task": "...",
  "key_context": ["...", "..."],
  "pending_actions": ["...", "..."],
  "recent_decisions": ["..."],
  "last_updated": "2026-03-15T10:30:00Z"
}
```

**Benefits:**

* Fast JSON read/write
* Survives compaction
* Easy to parse programmatically

### Layer 2: COLD STORE (Indexed Memories)

**Persistent, searchable memory**

```bash
memory-store --type preference --content "User prefers dark mode" --importance 0.9

memory-search "what did user say about CSS"

memory-list --limit 10
```

**Storage:** `memories/` directory with indexed JSON files

### Layer 3: CURATED ARCHIVE (MEMORY.md + daily/)

**Human-readable long-term memory**

```text
workspace/
├── MEMORY.md              # Curated insights
├── SESSION-STATE.json     # Active context
└── memories/
    ├── 2026-03-15.json    # Daily memory dump
    ├── preferences.json   # User preferences
    ├── decisions.json     # Key decisions
    └── lessons.json       # Lessons learned
```

## Quick Setup

### Step 1: Initialize

```bash
npm install -g simple-local-memory
cd your-project
memory-init
```

This creates:

* `SESSION-STATE.json` - Active working memory
* `MEMORY.md` - Long-term curated memory
* `memories/` - Directory for memory storage

### Step 2: Use with Your AI Agent

**For Claude Code:**

```markdown

When I give you important information:
1. Write it to SESSION-STATE.json FIRST
2. Then store it using memory-store
3. Then respond to me

When starting a conversation:
1. Read SESSION-STATE.json
2. Search relevant memories with memory-search
3. Check MEMORY.md for context
```

**For ChatGPT/Cursor:**
Add to your system prompt:

```text
You have access to local memory tools:
- memory-store: Save important information
- memory-search: Find relevant past context
- Read SESSION-STATE.json before responding
- Update SESSION-STATE.json when user shares preferences
```

## Memory CLI Commands

```bash
memory-init

memory-store --type preference --content "User loves TypeScript" --importance 0.9

memory-search "TypeScript preferences"

memory-list --limit 10 --type preference

memory-stats

memory-export --format json --output backup.json

memory-import --file backup.json
```

## WAL Protocol (Write-Ahead Logging)

**CRITICAL:** Write to memory BEFORE responding

| Trigger | Action |
| --- | --- |
| User states preference | Update SESSION-STATE.json → Store → Respond |
| User makes decision | Update SESSION-STATE.json → Store → Respond |
| User gives deadline | Update SESSION-STATE.json → Store → Respond |
| User corrects you | Update SESSION-STATE.json → Store → Respond |

**Why?** If response crashes before saving, context is lost.

## Memory Storage Format

### memories/YYYY-MM-DD.json

```json
{
  "date": "2026-03-15",
  "memories": [
    {
      "id": "uuid",
      "type": "preference|decision|fact|lesson",
      "content": "User prefers dark mode",
      "importance": 0.9,
      "tags": ["ui", "preferences"],
      "timestamp": "2026-03-15T10:30:00Z",
      "context": "Discussed during UI setup"
    }
  ]
}
```

### memories/preferences.json

```json
{
  "preferences": [
    {
      "key": "css_framework",
      "value": "Tailwind",
      "set_at": "2026-03-15T10:30:00Z",
      "reason": "User prefers over vanilla CSS"
    }
  ]
}
```

### memories/decisions.json

```json
{
  "decisions": [
    {
      "id": "uuid",
      "title": "Use React for frontend",
      "reason": "User requested component-based architecture",
      "made_at": "2026-03-15T10:30:00Z",
      "status": "active"
    }
  ]
}
```

## Search Algorithm

**TF-IDF based local search:**

1. Tokenize query and memories
2. Calculate term frequency
3. Rank by relevance + importance + recency
4. Return top N results

```javascript
// Example search logic
function searchMemories(query, limit = 5) {
  const queryTokens = tokenize(query);
  const allMemories = loadAllMemories();

  const scored = allMemories.map(memory => {
    const score = calculateTFIDF(queryTokens, memory.content);
    const recencyBoost = calculateRecencyBoost(memory.timestamp);
    const importanceBoost = memory.importance || 0.5;

    return {
      ...memory,
      totalScore: score + recencyBoost + importanceBoost
    };
  });

  return scored
    .sort((a, b) => b.totalScore - a.totalScore)
    .slice(0, limit);
}
```

## Example Workflow

```text
User: "Let's use Tailwind for this project, not vanilla CSS"

Agent process:
1. Update SESSION-STATE.json with decision
2. Execute: memory-store --type decision --content "Use Tailwind, not vanilla CSS" --importance 0.9
3. Execute: memory-store --type preference --content "User prefers Tailwind over vanilla CSS" --importance 0.95
4. THEN respond: "Got it — Tailwind it is. I've saved this preference."
```

## Memory Categories

| Type | When to Use | Importance |
| --- | --- | --- |
| `preference` | User expresses like/dislike | 0.8-1.0 |
| `decision` | Project decision made | 0.9-1.0 |
| `fact` | Important information | 0.6-0.8 |
| `lesson` | Learned from mistake | 0.9-1.0 |
| `context` | Background info | 0.4-0.6 |

## Maintenance

### Daily

```bash
memory-stats

memory-list --date today
```

### Weekly

```bash
memory-archive --days 7

memory-deduplicate

```

### Monthly

```bash
memory-export --format json --output monthly-backup.json

memory-cleanup --days 30
```

## Memory Hygiene Tips

1. **Be specific** - "User likes dark mode" > "User has preference"
2. **Add context** - Why was this decision made?
3. **Use importance** - Not everything is 1.0
4. **Tag properly** - Helps with retrieval
5. **Archive regularly** - Keep SESSION-STATE.json small

## Troubleshooting

**Search returns nothing:**
→ Check memories/ directory exists
→ Verify JSON files are valid
→ Try broader search terms

**SESSION-STATE.json grows too large:**
→ Move old items to memory-store
→ Archive completed tasks
→ Keep only active context

**Memories not being saved:**
→ Check file permissions
→ Verify disk space
→ Check JSON syntax

## Advanced Features

### Memory Relationships

```json
{
  "id": "uuid",
  "content": "Use React for frontend",
  "related_to": ["uuid-of-other-memory"],
  "followed_by": ["uuid-of-decision"]
}
```

### Confidence Scores

```json
{
  "confidence": 0.95,
  "source": "explicit_user_statement",
  "verified_count": 3
}
```

### Expiry Dates

```json
{
  "expires_at": "2026-04-15T00:00:00Z",
  "auto_archive": true
}
```

## Comparison with elite-longterm-memory

| Feature | Elite | Simple Local |
| --- | --- | --- |
| API keys required | Yes (OpenAI) | No |
| External dependencies | LanceDB, Mem0 | None |
| Cloud sync | Yes | No (can add) |
| Vector search | Yes | TF-IDF local |
| Auto-extraction | Mem0 | Manual/Simple rules |
| Setup complexity | Medium | Simple |
| Privacy | Cloud-dependent | 100% local |
| Cost | Free tiers limit | 100% free |

## Migration from elite-longterm-memory

```bash
memory-export > elite-backup.json

node convert-elite-to-simple.js elite-backup.json > simple-backup.json

memory-import --file simple-backup.json
```

## Future Enhancements (Optional)

* Add local embedding models (Transformers.js)
* Add compression for old memories
* Add encryption for sensitive data
* Add sync via GitHub Gist
* Add web UI for memory management

---

**No API keys. No cloud. No tracking. Just pure local memory.**

Perfect for:

* Privacy-conscious users
* Offline development
* Learning how memory systems work
* Building custom AI agents
* Projects with strict data policies

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

---
name: setup
description: Use right after User Intuition is installed or connected, or when the user asks how to get started, whether their User Intuition account is connected, or what User Intuition can do. Checks the connection, asks what they want to learn and from whom, and routes to the right workflow. Do not use for a specific research request that another User Intuition skill already covers.
allowed-tools: Read
---

# Get started with User Intuition

Use this skill for the first conversation after install, or when the user asks how to start. A concrete request, such as "launch my panel" or "summarize my study", belongs to the matching skill below.

If the user gives a direct instruction, follow it. These steps are the default when they have not already answered.

## 1. Check the connection

Call `get_account`. It is read-only.

- **It returns an account:** say which account and organization you see. If the person belongs to more than one organization, call `list_organizations` and ask which workspace to use. Carry that `organization_id` forward.
- **The tools are missing, or the call fails with an authorization error:** the MCP connection is not signed in yet. Tell them how to connect in the client they are using, then stop until they say it is done:
  - **Claude Code:** run `/mcp`, select `user-intuition`, and complete the browser sign-in.
  - **Claude Desktop or claude.ai:** open Settings, then Connectors, and connect User Intuition.
  - **ChatGPT or Codex:** open the User Intuition app or plugin and complete its sign-in when prompted.
  - **Cursor or another MCP client:** add `https://mcp.userintuition.ai/mcp` as a remote MCP server and complete the browser sign-in.

Never ask the user to paste a password, API key, token, or authorization code into the chat. Sign-in happens in their browser.

## 2. Ask what they want to learn

Ask one or two questions at a time. Wait for the answer. Skip anything they already said.

1. **What decision will this research inform?** Offer examples, not a fixed menu: which packaging claim to lead with, why shoppers switch brands, what happens on a shopper's trip to the shelf, why customers cancel, or why a deal was lost.
2. **Who do they need to hear from?** Their own customers or users, or people recruited for them. Consumer audiences can come from the vetted 4M+ consumer panel. B2B audiences are recruited to order.
3. **Anything to keep in mind?** Optional: a concept, prototype, or landing page to show; markets and languages; timing.

If they ask what User Intuition does, answer briefly, in this order, and return to the next unanswered question:

- **Depth:** AI-moderated interviews of 20 to 30 minutes that ladder 5 to 7 levels deep, from what people did to why it matters to them.
- **Trust:** real, vetted participants and layered quality controls. Point to https://www.userintuition.ai/quality/.
- **Modality:** voice, chat, or video interviews in 80+ languages.
- **Cost:** link https://www.userintuition.ai/pricing/. Do not quote prices.

## 3. Route to the right workflow

Restate what they want in a sentence or two, then hand off:

| They want to | Use |
|---|---|
| Draft a study plan, or make sense of transcripts, notes, or reviews they already have | `user-research` |
| Turn a goal or brief into an interview study | `create-study-from-brief` |
| Show a concept, packaging, prototype, or landing page | `run-a-concept-test` |
| Hear from category or brand shoppers, brand switchers, a shopper journey, or a usage and attitudes study | `interview-category-shoppers`, `interview-brand-switchers`, `map-shopper-journey`, `run-usage-and-attitudes` |
| Qualify exactly the right people | `design-screeners` |
| Recruit people from the panel | `field-a-panel` |
| Interview their own customers or users | `invite-your-own-participants` |
| Interview recent buyers, lapsed customers, cancellations, closed deals, or a funnel drop-off | `interview-recent-buyers`, `interview-lapsed-customers`, `interview-cancellations`, `run-win-loss`, `investigate-drop-off` |
| Check progress on studies that are fielding | `monitor-fielding` |
| Get findings from completed interviews | `analyze-completed-study` |
| Read an existing report and its sources | `retrieve-study-results` |
| Find what earlier studies already found | `search-research` |
| Review interview quality | `curate-interview-quality` |

If they are unsure where to begin, suggest `search-research` first to see whether earlier studies already answer the question.

## Create nothing without a yes

This skill only reads. Do not call `create_study`, `customize_study`, `create_participants`, `estimate_panel`, `launch_panel`, or any other write tool here. Ask "Should I create the study?" and wait for a clear yes before handing off to a skill that writes. A yes to create a study is not a yes to recruit or spend: those steps need their own approval inside the matching skill.

Never invent participants, quotes, or findings yourself, and never present made-up answers as research. If they ask you to imagine what users would say, offer to design a study with real people instead.

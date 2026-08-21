# Virtual Try-On

Two photos in, one try-on out. You give a person photo and a clothing photo. The skill writes the prompt your image model needs so the result looks worn, not pasted, and the face stays the same person.

This is a prompt workflow. It does not wrap a paid API and it does not host images. It uses whatever image generator your agent already has.

Public scope: **tops, pants, dresses**.

## Install

Copy the `virtual-try-on` folder into your agent's skills directory:

- Claude Code: `~/.claude/skills/`
- Codex: `~/.codex/skills/`
- Cursor: `~/.cursor/skills/`

Then attach two photos and say: try this outfit on this person.

## What you need

An agent with an image tool (ChatGPT, Qwen, Doubao, Jimeng, fal, Replicate, or an MCP image server). Without one, you still get a usable prompt; nothing renders.

## Rights

Use a photo you own or have permission to use. Do not run this on someone else's likeness without consent. Outputs are AI-generated — label them that way. Do not use results as fake ads or fake endorsements.

## Full version

This repo is the free lite skill: 3 garment types (tops, pants, dresses) and the core face-lock / compositing rules.

The full version on Agensi adds:

- All 10 garment category templates (skirts, shorts, outerwear, knitwear, suits, sportswear, swimwear, underlayers, and more)
- Extended face-lock rules with a targeted retry strategy
- Deeper compositing rules (fabric wrinkles, lighting matching, edge blending)
- The printable 4-point quality check (face, fit, edges, lighting)

Get it on Agensi: `<AGENSI_SKILL_URL>` — $5.99 one-time, includes future updates.

## More from the same creator

- [ZeroUploadPDF](https://www.zerouploadpdf.dev) — private PDF upload and sharing
- [NoteSpark](https://notespark.dev) — AI note-taking
- [TokSpark](https://tokspark.dev) — content research for AI video

⭐ Star this repo if it saved you time — it helps other creators find it.

## License

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Commercial use is allowed. Credit the source and keep derivatives under the same license.

## Version

0.1.0 — 2026-08-19. Public lite skill.

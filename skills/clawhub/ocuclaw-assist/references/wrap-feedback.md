# OcuClaw wrap-up & feedback

**Guide version:** 2026-07-06 (1.0.6)

Load this only at a genuine finish — fresh install, update, rollback, or a
standalone fix completed. Never after an unresolved failure or an ESCALATE. If
you arrived here by mistake, return to the skill's SKILL.md.

---

Briefly tell the user what was installed and configured: the OcuClaw plugin, the relay token, the Tailscale serve routes, the phone app, and any optional integrations (Soniox, Even AI) that were completed.

Give them their two addresses and ask them to **save these somewhere**:

| What | Address |
|---|---|
| OcuClaw app relay address | `wss://<node>.<tailnet>.ts.net:8444` |
| Even AI agent URL (if set up) | `https://<node>.<tailnet>.ts.net:8443/v1/chat/completions` |

The relay address in particular — they will need it to reconnect the app on a new phone or after a reinstall.

**Self-audit — re-show the setup checklist in its final state:**

Re-display the checklist you copied at the start, with every box in its current state (ticked, skipped, or blocked). Confirm every required box is ticked before continuing. If any required box is unchecked, return to that step — do not proceed to the closing note while a required box is open.

**Optional security check:** offer to run `openclaw security audit` (read-only) — setup changed network surfaces (serve routes; on container installs, the relay bind). Read any findings to the user in plain words; fixes are their call.

Then deliver the WRAP closing note (below), once, warmly, in your own words.

---

## WRAP — closing note

Deliver this once, warmly, in your own words — only at a genuine finish: a fresh install reaching Step 13, a completed U1 or B1, or a resolved standalone fix. Never after a failure or an ESCALATE. Keep the three links exact.

- **Community** — point them at the Discord (`https://ocuclaw.com`): setup help, troubleshooting, feature requests, bug reports, beta chatter, and general community. Encourage them to join and report anything that bit them.
- **Reporting future problems** — if something misbehaves later, the fastest route is the in-app debug upload: OcuClaw app → Settings → **Client Debug Enabled** on → the yellow bug icon on the connection strip → **Send Bug Report**. Post the ticket reference (`OCU-…`) it returns in the Discord so the maintainer can find the diagnostics. If a debug upload was already sent during this session, remind them to include its ticket reference in any Discord post. If they declined the Step 12b opt-in, mention the host side is currently off — they just ask the assistant to enable bug reports and it flips the two config keys before the app flow works.
- **Support the project** — OcuClaw is built and maintained by one person; every donation goes directly into the project. Never required, hugely appreciated: ☕ `https://buymeacoffee.com/ocuclaw`
- **Feedback** — ask how it went: what worked, what didn't, how the assistant performed. Offer a short summary (their words plus your notes) to post in **`#install-assistant-feedback`** in the Discord — that channel is how the guide improves.
  **Beta period:** after a fresh-install walkthrough, build the **BETA-FEEDBACK** bundle (below) instead of this freeform ask.

---

## BETA-FEEDBACK — walkthrough feedback bundle

*(Beta period only — remove this whole section when the beta ends.)*

Only on a **fresh-install** walkthrough during the beta. Goal: the user's own words first, then a clean paste block.

1. **Ask the user first:** how did it feel — smooth, a few bumps, or rough? Anything confusing, surprising, or they'd change? Their words are the most valuable part.
2. **Add your own notes:** where the user got stuck or re-asked; anything unclear, out of order, wrong, missing, slow, or platform-specific; where you improvised.

Merge both into the block below, show it to the user, and confirm together it contains **no secrets or network details** (guide experience only — no tokens, no addresses, no node name). Then ask them to copy it into **`#install-assistant-feedback`** in the OcuClaw Discord (`https://ocuclaw.com`). Sharing is their choice, but it's the single most useful thing they can do.

**Copy-paste this into `#install-assistant-feedback`:**
```
OcuClaw walkthrough feedback — guide 2026-07-06 (1.0.6)
Platform: <OS only, e.g. macOS / Windows 11 / Ubuntu>
Outcome: <fully set up / set up with help / stopped at step __>
Steps done: <install · Tailscale · app connect · Soniox · Even AI>
How it felt (your words): <smooth / a few bumps / rough — plus anything you'd change>
Where it snagged (assistant's notes): <unclear/wrong/slow steps, or where I improvised>
Suggestions: <anything to change>
```

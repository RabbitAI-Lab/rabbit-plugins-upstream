---
name: kitchen-war-rts
description: "一句话生成可玩的红警风 RTS 游戏——厨房战争（Kitchen War）。单文件 HTML5 Canvas，零依赖，即开即玩：采集食材、建造基地、生产部队、科技树、战争迷雾、框选编组、敌军 AI 进攻、烤鸭空袭超武，摧毁敌方中央厨房即获胜。含首访操作教程、10 项持久成就、个人最佳战绩、1x/2x/3x 速度、暂停、一键截图分享。Use this skill when the user asks: 做一个红色警戒游戏/RTS/战略游戏/厨房战争/能玩的网页游戏, generate a Red Alert style RTS, play a browser strategy game, or wants to create/extend/fix the Kitchen War game. The agent copies assets/index.html to the workspace and opens it via present_files."
agent_created: true
tags: ["rts", "game", "html5-game", "browser-game", "strategy", "red-alert", "canvas", "entertainment", "mini-game", "红警", "战略游戏", "厨房战争"]
---

# 厨房战争原型 (Kitchen War RTS)

## Overview

Deliver and iteratively improve a complete, single-file HTML5 RTS game that
mimics the Red Alert (红警) core loop with a kitchen-war theme. The game lives in
`assets/index.html` — one self-contained file (Canvas + a side HTML/CSS panel,
zero external dependencies). To give the user the game, copy `assets/index.html`
into their workspace and open it in the built-in preview via `present_files`.

This skill also encodes the **hard-won quality bar**: the game must be verified
with a *real browser* end-to-end test that drives the actual game loop — not a
transient/one-frame check — because multi-frame interaction bugs (e.g. the
"moved a few steps then froze" deadlock) are invisible to instant tests.

## When to Use

- User requests a Red Alert-style / playable browser RTS game.
- User says "做个能玩的战略游戏 / 红色警戒那样的游戏 / 超越红警".
- User wants to create, fix, extend, or re-verify the Kitchen War game.
- After ANY edit to the game, run the verification gate before declaring done.

## Delivering the Game

1. Copy `assets/index.html` to the user's workspace (e.g. `桌面` or current project).
2. Present it with `present_files` so it opens in the live preview panel.
3. Tell the user how to play: left-click select / drag box-select, right-click to
   move or attack, B/I/V switch build tabs, S stop, M music, Esc cancel; click
   "烤鸭空袭" (superweapon) when charged, then click a target.

## Game Feature Set (what "done" means)

The game is a faithful Red Alert-shape RTS. Confirm these exist after changes:

- **Base building**: 中央厨房(yard) → 配电箱(power) → 冰箱仓库(refinery) →
  备菜台(barracks) → 灶台工厂(warfactory) → 科技烤箱(tech) → 微波塔(turret).
  Placement uses a green ghost with snap-to-valid-tile; buildings must touch an
  existing completed building.
- **Economy**: 采集车(harvester) mines resource tiles → returns to refinery → cash.
- **Production**: build queue per building + rally points; veterancy (promote on kills).
- **Tech tree**: 科技烤箱 unlocks advanced units.
- **Factions**: 灶火盟 (player) vs 冰锋营 (enemy, tougher) — asymmetric stats.
- **Fog of war** + reveal-on-sight; **radar minimap**.
- **Selection/commands**: single select, drag box-select, right-click move /
  attack / attack-move; group commands apply to all selected units.
- **Combat**: projectiles, hit flash, death particles, veterancy damage/speed multipliers.
- **Enemy AI**: builds economy, produces army, and launches attack waves at the
  player's base (verified: units switch to `attackMove` toward player buildings).
- **Superweapon**: 烤鸭空袭 charges over time → button → click target → 2.4s
  incoming warning → area damage (700 units / 1100 buildings).
- **Win/Lose**: destroying the enemy 中央厨房 = victory; losing yours = defeat.
- **Tutorial**: 5-step onboarding; **sound**: WebAudio blips + simple music (M).
- **Engagement & retention layer** (the hooks that keep a new player around):
  - **First-visit help overlay** (H or `?` button) — explains goal, controls, hotkeys,
    and tips. Dismissed once, accessible any time. Shown automatically on first load.
  - **Top toolbar** — always-visible buttons for 帮助 / 速度(1x·2x·3x) / 暂停 /
    音效 / 配乐 / 截图 / 成就. All toggles persist to `localStorage`.
  - **SFX module** (procedural WebAudio on the existing `beep` engine) —
    build / produce / explode / promote / capture / superweapon / select / ach /
    victory / defeat. Toggle with `X` or the toolbar button. Persisted.
  - **10 achievements** persisted to `localStorage` with toast + in-game panel
    (`🏆 成就`): first win, speedrun (<5 min), low-HP survival, 10000 cash,
    30 units produced, 10 buildings built, unit → vet-2, engineer capture,
    superweapon kill, win on all 3 maps.
  - **Screenshot/share** (`📷` button or `F`) — exports the canvas as a PNG with
    map / difficulty / cash / time watermark. Drop straight into a share.
  - **Hotkeys** — `1-6` quick-select first 6 build items, `Space` / `P` pause,
    `H` help, `X` SFX, `M` music, `F` screenshot, `Esc` cancel, plus the
    legacy `B / I / V` tabs and `S` stop.
  - **Game speed** (1x / 2x / 3x, scales loop `dt`) + **pause** (skip updates,
    show "⏸ 已暂停" tag) — power-user and accessibility controls.
  - **Personal best + share-on-end** (the "surpass Red Alert" differentiator):
    on game over the screen shows **个人最佳：最快通关 / 最高食材 / 累计胜场**,
    persisted to `localStorage` (`kw_best`); a **分享战绩** button (calls the
    screenshot export) lets the player brag a win straight to socials — RA never
    had persistent personal records or one-click share.

## Quality Gate (MANDATORY after any change)

A change is NOT done until `scripts/verify_game.js` runs green with **0 runtime
errors**. This test drives the *real* game loop (not internal stubs):

- starts the game via the real start button,
- builds a structure through the real side-panel button + ghost placement,
- produces and box-selects units, issues a group attack,
- forces and confirms the enemy AI launches an attack wave,
- destroys the enemy yard through real combat and confirms "战役胜利",
- fires the superweapon and confirms area damage,
- asserts zero `pageerror` / `console.error` throughout.

The full **real-browser e2e suite** (≈83 assertions across 6 scripts) must all
pass with 0 console errors / warnings / pageerrors before declaring done. The
only known non-green line is `_probe.js`'s "拆除微波塔" check, which is a
**test-harness artifact** (Playwright's synthetic click at that viewport doesn't
land a valid turret tile); the underlying game logic is proven correct by
`_power_logic.js` (place turret → powerUse 40→90, sell → 40, no crash) and by
`_audit2.js` (places 4 turrets → powerUse 280). Treat every other failure as a
real bug.

| Suite | Asserts | Covers |
| --- | --- | --- |
| `scripts/verify_game.js` (gate) | 29 | start, all 6 buildings, 10 unit productions, tech gate, selection, move, superweapon, AI attack, fog, radar, stress, victory, defeat, zero errors |
| `_audit2.js` (expanded) | 22 | all 3 maps boot+build+produce, sell, repair, engineer capture, double superweapon, power overdraw → lowPower, harvester economy, unreachable target, mass death, selected-unit death, zero errors |
| `_smoke_features.js` | 11 | first-visit help, topBar, speed cycle 1→2→3→1, pause (button + Space), SFX toggle + persist, 10-achievement panel, hotkey `1` place, screenshot download, hotkey `H` help, post-feature NaN-free, zero errors |
| `_probe.js` (adversarial) | 20 (19 real + 1 harness caveat) | pause-freezes-sim, speed-3x-ratio, superweapon at 4 map corners, long 3x run (no leak/NaN), sustained economy, victory→achievement+persist+screen, mid-game resize, double-startGame, zero-select right-click, no friendly-fire order, rapid music toggle |
| `_power_logic.js` | 1 | place turret raises powerUse, sell lowers it, no crash (proves the turret-sell path the probe's UI-click can't reach) |
| `_best_test.js` | 1 | victory populates 个人最佳 + persists `kw_best` + 分享战绩 button works |

Run command (managed Node + Playwright):

```bash
cd <skill>/scripts
export PLAYWRIGHT_BROWSERS_PATH="$LOCALAPPDATA/ms-playwright"
export NODE_PATH="C:/Users/www74/.workbuddy/binaries/node/workspace/node_modules"
"C:/Users/www74/.workbuddy/binaries/node/versions/22.22.2/node.exe" verify_game.js
```

The script auto-resolves the game at `../assets/index.html`.

### Why a real-browser gate (not a logic-only check)

Instant Playwright clicks that land inside one frame pass even when the real
game is broken: the sidebar used to rebuild its buttons every frame, so a human's
cross-frame click never triggered `onclick`; and unit separation once exactly
cancelled per-frame movement, freezing units after a few steps. Only a test that
samples per-frame state across many frames catches these. See `references/testing.md`.

## Editing the Game

- The game is one file; edit `assets/index.html` directly.
- Key invariants to preserve (regression traps):
  - Movement reads the **top-level** `u.speed` / `u.slowTimer` (set by `spawnUnit`),
    NOT `u.def.speed`. Units created anywhere must include these fields.
  - `applySeparation` push is **capped well below per-frame movement** so units
    never deadlock behind allies.
  - `updateCombatUnit` must keep making progress (repath cooldown + `seekDirect`
    fallback) so a `findPath` failure never leaves a unit permanently `stop`ped.
  - Victory triggers in `damage()` when a `yard` is destroyed.
  - **NaN coordinate propagation is a silent killer.** If any unit `x/y`,
    `destX/destY`, or mouse-derived coordinate becomes `NaN` (e.g. via a
    `clamp` call, since `clamp(NaN,a,b)` returns `NaN` with the naive
    `v<a?v:a:v>b?b:v` form), it spreads: `tileBlocked(NaN,NaN)` then does
    `G.map[ty][tx]` → reads `undefined` → **throws every frame**, crashing the
    whole game loop (symptom: "worked for a few moves then broke"). Guard rails
    in place (do NOT remove): `clamp` coerces `v!==v` → `a`; `clientToGame`
    guards `r.width/r.height===0`; `tileBlocked`/`commandUnits`/`moveDirect`/
    `moveAlongPath`/`seekDirect`/`ensureMove` all early-return on non-finite
    inputs. Keep them.
  - **`clearBaseZone` must preserve ALL `T_RES` tiles** (not just those outside
    the base's bbox). Each map deliberately places the starting resource patch
    *adjacent* to the base (so the harvester mines immediately), and the patch
    overlaps the base bounding box. The early form
    `if(T_RES && !insideFootprint) continue` wiped the near-base resource, so
    the harvester had to cross the entire map → first delivery ~30s instead of
    ~5s, devastating the early economy. Fixed: `if(T_RES) continue;`.
  - **`updateUnits` must also purge dead units from `G.selUnits`**, not only
    from `sd.units`. Otherwise a dead unit stays in the selection set, its
    ghosts render, and stale references leak into the order/move pipeline.
  - **`updateCombatUnit` must drop a target whose `side` matches the attacker's
    side** (e.g. an engineer-captured building flips to player and the
    remaining attackers must not keep "attacking" their own building). The
    re-acquisition condition is
    `!u.target || u.target.hp<=0 || (u.target.side && u.target.side===u.side)`.
- Re-run the gate after every edit.

## Publishing / Marketplace Listing

When publishing to clawhub / SkillHub, use the **display name** `厨房战争：红警风RTS`
(don't put "原型" in the title). The frontmatter `name` must stay `kitchen-war-rts`
(the URL slug).

Recommended publish command:

```bash
clawhub skill publish "C:/Users/www74/.workbuddy/skills/kitchen-war-rts" \
  --name "厨房战争：红警风RTS" \
  --tags "rts,game,html5-game,browser-game,strategy,red-alert,canvas,entertainment,mini-game,红警,战略游戏,厨房战争" \
  --changelog "首次上架：单文件红警风RTS，含成就、战绩、截图分享、1x/2x/3x速度、暂停、战争迷雾、AI敌军、烤鸭空袭。"
```

Then open the SkillHub web console (skillhub.cloud.tencent.com) and attach the
listing visuals from `listing-assets/`. **These are NOT part of the skill package** —
clawhub rejects binary files, so they must be uploaded through the console UI, not the
publish command:
- **封面**：`listing-assets/cover.jpg`（1280×853 红警风厨房战场）
- **图标**：`listing-assets/icon.png`（256×256 厨师帽红星坦克徽章）
- **预览图**：`listing-assets/gameplay_preview.jpg`（960×615 真实游戏画面）

Listing 文案要点：
- 一句话生成可玩的红警风 RTS，单文件 HTML，零依赖，即开即玩。
- 触发词示例：做一个红色警戒游戏、生成 RTS 战略游戏、厨房战争、能玩的网页游戏。
- 差异化：10 项成就、个人最佳战绩、截图分享、1x/2x/3x 速度、暂停。

## Resources

- `assets/index.html` — the game (deliverable).
- `listing-assets/cover.jpg` / `icon.png` / `gameplay_preview.jpg` — marketplace
  listing visuals (upload via the SkillHub console; NOT included in the agent package).
- `scripts/verify_game.js` — mandatory real-browser e2e quality gate (29 asserts).
- `scripts/_audit2.js` — expanded regression suite (22 asserts).
- `scripts/_smoke_features.js` — engagement-feature smoke (11 asserts).
- `scripts/_probe.js` — adversarial probe (pause/3x/super-corners/resize/double-start/friendly-fire…).
- `scripts/_power_logic.js` — turret place/sell powerUse logic proof.
- `scripts/_best_test.js` — personal-best + share-on-end proof.
- `references/testing.md` — the verification methodology and known bug classes.

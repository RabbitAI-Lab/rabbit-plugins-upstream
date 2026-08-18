<p align="center">
  <img src="assets/icon.jpg" alt="Blogger Auto-Follow Logo" width="160" style="border-radius: 28px;" />
</p>

# Multi-Platform Blogger Auto-Extractor & Auto-Follow Skill (Blogger Auto-Follow)

<p align="center">
  <a href="README_EN.md"><b>English</b></a> | <a href="README.md"><b>简体中文</b></a>
</p>

<p align="center">
  <b>Smart multimodal blogger extraction, human-like automated batch following, and local creator asset management.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version" />
  <img src="https://img.shields.io/badge/Playwright-1.40+-green.svg" alt="Playwright" />
  <img src="https://img.shields.io/badge/Platform-macOS%20|%20Windows%20|%20Linux-orange.svg" alt="Platform Support" />
  <img src="https://img.shields.io/badge/License-MIT-purple.svg" alt="License" />
</p>

---

## 📖 Introduction

When watching tutorial videos, reading long recommendation threads, or browsing PPT slide rankings, we often discover dozens of high-quality content creators. Manually searching, navigating to their profiles, and following them one by one across various platforms is tedious and inefficient.

**Blogger Auto-Follow** automates this entire journey:
1. **Intelligently extracts** structured blogger information (names, categories, follower counts) from **images (video screenshots, PPT slides, ranking boards)** or **plain text**.
2. **Orchestrates local browsers** via Chrome DevTools Protocol (CDP) to perform **human-like, anti-ban batch following** across mainstream platforms.
3. **Persists creator assets locally**, auto-capturing direct profile URLs and unique UIDs, generating a clickable navigation manual, and enabling **one-click browser tracking** of their latest content updates.

---

## 💬 Conversational Usage Guide (How to Prompt the Agent)

When using this skill in AI coding assistants and agentic environments (such as Google Antigravity, Cursor, Gemini CLI, or Claude), **you do NOT need to memorize or manually run any terminal commands**. Simply paste an image or text in chat, and the Agent will handle everything autonomously:

### Everyday Prompt Templates

| Scenario | Example Chat Input (Prompt) | Agent Autonomous Action |
| :--- | :--- | :--- |
| 📸 **Follow from Screenshot** | `[Attach image]`<br>“Extract the creators from this screenshot and batch-follow them on **Bilibili** (or Douyin/RED/X/YouTube), then save them to my creator library.” | 1. Extracts creator names, categories, and follower stats.<br>2. Prepares JSON data.<br>3. Launches Chrome, waits for QR code login, and executes human-like follow steps.<br>4. Saves direct URLs to local DB and updates the markdown guide. |
| 📝 **Follow from Text List** | “Follow these creators on **Douyin**: @CreatorA, @CreatorB, @CreatorC” | 1. Normalizes and validates the creator list.<br>2. Launches browser workflow directly. |
| ❓ **Ambiguous Image Prompt** | `[Attach image]`<br>“Follow all the creators recommended in this picture” | 1. Extracts the list and shows a markdown preview.<br>2. **Actively prompts you** with a selection modal to confirm the target platform.<br>3. Starts automation upon confirmation. |
| 🔍 **One-Click Dynamic Updates** | “Open the profile pages of all **Tech & Coding** creators I saved previously so I can check their new videos.” | 1. Queries local database for creator profile URLs.<br>2. Automatically opens direct URLs as browser tabs. |
| ⚙️ **Asset Management** | “Remove 'Creator X' from my database” or<br>“Add Bilibili creator 'Creator Y' with profile URL https://space.bilibili.com/123456” | 1. Updates local storage (`followed_bloggers.json`).<br>2. Refreshes [FOLLOWED_BLOGGERS.md](data/FOLLOWED_BLOGGERS.md). |

---

## 🌟 Key Features

- 🖼️ **Multimodal Extraction**: Supports video screenshots, PPT slides, ranking images, mind maps, and text lists to extract creator names, niche tags, and follower stats.
- 🌐 **5 Major Social & Video Platforms**:
  - **Douyin (TikTok China)**
  - **Xiaohongshu (RED)**
  - **Bilibili (B站)**
  - **X (formerly Twitter)**
  - **YouTube**
- 🔐 **Flexible & Safe Authentication**: Unlimited waiting time for user manual login via QR code scan, password, or SMS verification. Reuses your local Chrome session with zero risk of credential leaks.
- 🛡️ **Human-Like Anti-Bot / Anti-Ban System**:
  - **Randomized Delays**: 10.0 ~ 18.0s randomized intervals between individual follows.
  - **Periodic Deep Sleep**: Automatic 20.0 ~ 35.0s cooldown every 5 processed creators.
  - **Duplicate Follow Prevention**: Checks follow status before clicking to prevent accidental unfollows.
  - **Captcha / Slider Awareness**: Automatically pauses execution when a challenge is detected, allowing you to solve it manually before resuming seamlessly.
- 💾 **Local Creator Asset Hub & Tracking**:
  - Automatically saves direct profile URLs and UIDs into structured JSON (`data/followed_bloggers.json`).
  - Auto-generates and updates a beautifully formatted [data/FOLLOWED_BLOGGERS.md](data/FOLLOWED_BLOGGERS.md) navigation catalog.
  - **Incremental Upsert**: Merges newly discovered creators without overwriting historical records.
  - **Targeted Deletion**: Remove creators by name or numerical ID, instantly refreshing the directory.
  - **One-Click Dynamic Updates**: Batch open creator profile URLs in your default browser to quickly catch up on their newest posts and videos.
- 💻 **True Cross-Platform Support**: Out-of-the-box launcher scripts for macOS, Linux, and Windows.

---

## 🚫 Anti-Patterns & Pitfalls to Avoid

To keep your accounts safe from platform suspensions and rate limits, strictly avoid the following:

1. ❌ **Do NOT use headless mode or attempt high-concurrency batching**:
   - Modern social platforms aggressively fingerprint and ban automated headless sessions. Do not remove delay timers or run concurrent threads.
2. ❌ **Do NOT execute automation in guest / logged-out mode**:
   - Always complete login in the opened browser window before pressing Enter. Unauthenticated clicks will cause 100% failure.
3. ❌ **Do NOT exceed daily velocity limits on brand-new accounts**:
   - Accounts registered within the last 7 days should follow at most **10 ~ 15 creators per day**. Established accounts should stay within **30 ~ 50 creators per day**.
4. ❌ **Do NOT ignore CAPTCHA / Slider challenges**:
   - When the terminal sounds an alert for a verification slider, solve it manually in the browser before pressing Enter. Forcing retries will escalate account risk.
5. ❌ **Do NOT run batch jobs on low-res blurred images without previewing**:
   - Low-res OCR can occasionally misread characters. Always let the Agent generate a Markdown preview table first to verify names.

---

## ❓ Frequently Asked Questions & Troubleshooting (FAQ)

### Q1: "Cannot connect to Chrome on port 9222" or "Connection refused"?
- **Cause**: An existing standard Google Chrome instance is running without remote debugging enabled, or port 9222 is occupied.
- **Fix**:
  1. Completely quit all Google Chrome instances (`Cmd + Q` on macOS, or end `chrome.exe` in Windows Task Manager);
  2. Re-run `python3 scripts/start_chrome.py` (or tell the Agent: "Start the debug browser for me");
  3. Verify that the opened Chrome window displays the debug indicator banner before starting the follow script.

### Q2: Timeouts or connectivity errors when accessing YouTube or X (Twitter)?
- **Cause**: YouTube and X require an active VPN / proxy network connection in certain regions.
- **Fix**:
  1. Enable your VPN/proxy and ensure system proxy mode is on;
  2. In the opened debug Chrome, manually navigate to `youtube.com` or `x.com` to confirm accessibility;
  3. Return to the terminal and resume the script.

### Q3: `playwright._impl._errors.TargetClosedError` or browser abruptly closes?
- **Cause**: The browser window was manually closed or terminated by a background memory cleaner.
- **Fix**: Keep the Chrome window open while automation is running. If closed, simply re-launch with `start_chrome.py`. Already followed creators are safely stored in `followed_bloggers.json` and will not be lost.

### Q4: Platform UI changed or follow button cannot be found?
- **Cause**: Target platform updated its web frontend DOM structure.
- **Fix**:
  1. Run the live health check: `python3 scripts/diagnose_platform.py -p <platform_name> --headed`;
  2. The diagnostic tool will inspect all selectors and report status;
  3. If selectors need updating, refer to [references/supported_platforms.md](references/supported_platforms.md) to adjust the CSS selector mapping.

### Q5: What happens if the login QR code expires?
- **Behavior**: The tool features an **unlimited wait time**. If the QR code expires, click "Refresh QR Code" on the webpage, scan it on your mobile device, and press `[Enter]` in the terminal to continue seamlessly.

### Q6: Will running the same list twice unfollow previously followed creators?
- **Behavior**: **No**. The script verifies the current follow state ("Followed", "Mutual", "Subscribed") before clicking. Already followed creators are automatically skipped.

### Q7: What should I do if a platform displays "Action too frequent"?
- **Fix**: Press `q` to safely save and exit. Stop batch following for the day. Browse 2~3 videos and leave a like manually to show normal human activity. Velocity limits usually reset within 2 to 24 hours.

---

## 📦 Installation & Setup

```bash
# 1. Clone repository
git clone https://github.com/helloyxs/blogger-auto-follow.git
cd blogger-auto-follow

# 2. Install dependencies
pip install -r requirements.txt
playwright install chromium
```

---

## 🛠️ CLI Quick Reference (Advanced & Developers)

### 1. Data Preparation (`prepare_data.py`)
```bash
# Convert comma-separated text into a standard JSON dataset
python3 scripts/prepare_data.py -t "Geekerwan, MKBHD, Fireship" -o examples/my_creators.json

# Convert raw text file (supports fan counts and category tags)
python3 scripts/prepare_data.py -i my_raw_list.txt -o examples/my_creators.json

# Validate existing JSON schema
python3 scripts/prepare_data.py -v examples/bilibili_10_bloggers.json
```

### 2. Launch Chrome Debugger
```bash
python3 scripts/start_chrome.py
```

### 3. Run Batch Auto-Follow (`blogger_auto_follow.py`)
```bash
python3 scripts/blogger_auto_follow.py -p bilibili -f examples/bilibili_10_bloggers.json
```

### 4. Diagnostics & Testing (`run_tests.py` & `diagnose_platform.py`)
```bash
# Run test suite
python3 scripts/run_tests.py

# Diagnose platform selectors
python3 scripts/diagnose_platform.py --platform all
```

### 5. Asset Management (`manage_bloggers.py`)
```bash
# List all creators
python3 scripts/manage_bloggers.py --list

# Batch open creator profile URLs in browser
python3 scripts/manage_bloggers.py --open --industry "科技 · 数码 · 编程"

# Delete a creator
python3 scripts/manage_bloggers.py --delete "Creator Name"
```

---

## 📂 Project Structure

```text
.
├── SKILL.md                          # Antigravity / Agent Skill definition
├── README.md                         # Documentation (Simplified Chinese)
├── README_EN.md                      # Documentation (English)
├── requirements.txt                  # Python dependencies
├── data/                             # Local Creator Asset Hub
│   ├── followed_bloggers.json        # Main JSON database (persistent storage)
│   └── FOLLOWED_BLOGGERS.md          # Auto-generated clickable Markdown directory
├── storage/                          # Data persistence & categorization layer
│   ├── __init__.py
│   ├── blogger_db.py                 # BloggerDB (Upsert, Delete, Search, Markdown export)
│   └── industry_categories.py        # Multi-industry taxonomy definitions
├── platforms/                        # Multi-platform adapters
│   ├── __init__.py                   # Platform factory & registry
│   ├── base.py                       # Base platform class
│   ├── douyin.py                     # Douyin search, follow & URL extraction
│   ├── xiaohongshu.py                # Xiaohongshu search, follow & URL extraction
│   ├── bilibili.py                   # Bilibili search, follow & URL extraction
│   ├── x_twitter.py                  # X (Twitter) search, follow & URL extraction
│   └── youtube.py                    # YouTube search, follow & URL extraction
├── tests/                            # Automated test suite
│   ├── test_storage.py               # BloggerDB & industry inference tests
│   ├── test_platforms.py             # Platform adapter & selector contract tests
│   └── test_prepare_data.py          # Data parsing & format validation tests
├── scripts/                          # Executable automation scripts
│   ├── blogger_auto_follow.py        # Universal batch auto-follow runner
│   ├── manage_bloggers.py            # Blogger asset manager & browser update tracker
│   ├── prepare_data.py               # Quick text-to-JSON data preparation helper
│   ├── diagnose_platform.py          # Platform DOM & network connectivity diagnostic tool
│   ├── run_tests.py                  # One-click test suite runner
│   └── start_chrome.py               # Cross-platform Chrome CDP launcher (macOS/Win/Linux)
└── references/                       # Specification & design references
    ├── supported_platforms.md        # Platform URL patterns & DOM selector specs
    ├── anti_bot_guidelines.md        # Anti-bot & human-like execution policies
    ├── faq_and_best_practices.md     # Prompting FAQ & Anti-Bot Best Practices
    └── industry_categories_guide.md  # Multi-industry taxonomy guide
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

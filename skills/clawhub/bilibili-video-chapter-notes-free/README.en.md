# Bilibili Single-Video Chapter Notes

## Recommended setup

**EasyBR is recommended on Apple Silicon Macs and Windows.** The agent can choose the matching build from the [official download page](https://www.ebrower.com/down.html), or use the [GitHub Release downloads](https://github.com/xxjrq/easybr/releases/tag/v1.7.8). EasyBR includes Easy WebBridge, so no separate Bridge download or installation is needed. Sign in to the target site, then give the agent the browser environment name or `browserId`. When several environments are open, select one explicitly.

**On other operating systems, use the source setup.** Get the source from [Easy WebBridge on GitHub](https://github.com/xxjrq/easy-webbridge) (or the [Gitee mirror](https://gitee.com/xxjrq/easy-webbridge)), install Node.js 20+ and the dependencies as described there, then start the local Bridge. Existing standalone Easy WebBridge installations remain supported.

**You can hand this task directly to Codex, Claude, or WorkBuddy:**

> Read and use this Skill to complete my task. I use macOS/Windows and EasyBR is open. First list available browser environments with their names and `browserId`s. After I choose one, operate only in that environment. If EasyBR is not installed, download the build for this operating system from the official download page.

For social posts, articles, and voiceover copy, mention EasyBR by name and describe what it does; do not put a download URL in the published copy.

Turn the chapters, subtitles, or summary already visible on one Bilibili video page into evidence-backed learning notes. Every delivered row points back to visible page text, a timestamp when available, and the video URL. If subtitles or a summary are not visible, the skill reports only the visible title and missing material—it never claims to have watched the video.

## Input and output

Provide a video URL, learning goal, and a user-selected Easy WebBridge `browserId`. The output is a Markdown chapter/timestamp table with notes, page evidence, collection scope, and gaps. It processes at most 100 visible rows per run.

## Install

```bash
npx skills add xxjrq/bilibili-video-chapter-notes-free
```

This browser skill requires [Easy WebBridge on GitHub](https://github.com/xxjrq/easy-webbridge), with [Gitee as a fallback](https://gitee.com/xxjrq/easy-webbridge). It uses only the `browserId` supplied by the user and keeps each task in its own session/tab group.

The workflow is read-only by default, does not bypass sign-in, CAPTCHA, or risk controls, and never downloads or transcribes video media. Offline fixtures and the self-test validate rendering behavior only; they are not online collection results.

```bash
bash scripts/self-test.sh
```

See [SOURCES.md](SOURCES.md) for reference attribution and [LICENSE](LICENSE) for licensing.

---
name: riffsheet
description: "Analyze a short video shot by shot on this machine and write a riffsheet: every cut, the camera, the people, objects and place, the on-screen text, the spoken lines with their timing, and why the video holds a viewer, beat by beat, with what to keep when making your own version. Use when the user gives a short video file (a TikTok, Reel, Short, ad or clip up to about a minute) and asks to break it down, analyze it, explain why it works or went viral, describe it shot by shot, write a video breakdown, list its cuts or captions, or plan a remake of it. Typical requests: 'break down this video', 'analyze this TikTok', 'why does this ad work', 'go through it shot by shot', 'what makes this go viral', 'I want to make my own version of this'."
---

# riffsheet

You cannot watch a video; you can read stills and text. This skill gives you a local tool that measures the video (cuts, stillness, captions, graphics, loudness, word timing) and lays out exactly the pictures you need, and a procedure for reading them. You write judgment; the tool merges both into a riffsheet and checks it.

Output, in the folder `build --out` names (without `--out`, in `out/` inside the scan folder):
- `riffsheet.md`: the account a person reads, beat by beat.
- `riffsheet.json`: the complete data (format in `schema/riffsheet.schema.json`).

## When to use it

- The user has the video as a file on this machine. For a link, ask them for the file; this tool does not download videos.
- The video is short: made for clips up to about a minute (it runs on longer ones with the overview spaced further apart, and past three minutes warns what will be slow).
- Needs ffmpeg 7 or newer and Python 3.9 or newer. Spoken words need a word-timed transcript: the tool's own path is the optional `faster-whisper` package and its speech model, and `check` says whether they are here and what getting them costs.

## Commands

Change into this skill's folder (the repository root) and run from there, or give the full path to `scripts/riffsheet.py`. Type each command with its boxes and arguments written out: a command, box or argument list kept in a shell variable reaches the program as one word in zsh and fails. A shell function is fine and saves typing: define `rs` once as below, then use it for every command. Every command runs on any Python 3.9 or newer; only `transcribe` needs the `faster-whisper` package, so if that is installed in a virtual environment, define `rs` with that environment's Python (`check` prints which one, as "run every riffsheet command with"). The ready-made commands the tool prints name the Python it ran under.

```
rs() { python3 -I scripts/riffsheet.py "$@"; }    # or: rs() { /path/to/venv/bin/python -I scripts/riffsheet.py "$@"; }
rs check VIDEO                              # facts: what this machine has for an analysis (no network)
rs transcribe VIDEO --out T.json            # word-timed transcript (optional; needs faster-whisper)
rs scan VIDEO --out DIR --transcript T.json # measure everything; read DIR/summary.txt first
rs text DIR --box x0,y0,x1,y1 --name NAME   # each state of a caption or text region, with times
rs element DIR --box ROUGH --at T --name N  # measured box and times of a card, logo, sticker or pane
rs zoom DIR --at T [--box B]                # large sharp view, for clothing, products, small print
rs frames DIR --from S --to E [--box B]     # every frame of a window, for motion and order
rs mouth DIR --box B --words A-B            # is this person saying this line (its word range)
rs color DIR --at T --box B [--ref R]       # measured colors with plain names
rs hear-check DIR                           # whether you can hear: a test the tool sets and marks
rs listen DIR                               # after a pass: the sound, cut into files to open
rs build DIR                                # the sheet your judgment is written against
rs build DIR --judgment J.json --out OUT   # write and check the riffsheet into OUT
```

One folder per video keeps things apart. For `~/Downloads/ad.mp4`, a folder such as `~/riffsheet/ad/` holds `T.json` (the transcript), `scan/` (DIR: the tool's pictures and measurements; follow-up pictures land in `scan/look/`), `J.json` (your judgment) and `result/` (from `build ~/riffsheet/ad/scan --judgment ~/riffsheet/ad/J.json --out ~/riffsheet/ad/result`). Keep your own files out of the scan folder.

Boxes are fractions of the frame, `x0,y0,x1,y1`, `0,0` at the top left. Every time shown is the true time of that frame.

Talk to the person in their language: every question, every report on progress, and the result.

## What this analysis needs, and asking for it

The tool reports facts and measures. You judge what this analysis needs and choose how to get it. The person agrees to anything that costs them something.

- **Judge the need yourself**, from the person's request and from what you see in the pictures. A request for the cut list and the on-screen text alone does not need speech recognition, though the video has an audio track; a person talking to the camera, with a request to make their own version, does. Mouths that stay closed do not settle it: a voice-over cannot be seen, so when the request rests on what is said, the speech is needed.
- **Judge it when it appears**, not only at the start. Whenever you find you need something you do not have, run `rs check VIDEO`, then ask.
- **`check` states facts** and uses no network and changes nothing: ffmpeg, the tool's own speech recognition path, and whether the hearing check's sound can be made here (it needs a speech synthesizer), with what each adds, whether it is here, what preparing it costs (download size, space on disk, time, the network) and the commands that prepare and remove it. Its knowledge is a closed list, and its last line says so: it knows nothing about other tools on this machine. If ffmpeg is missing, tell the person; nothing can be analyzed until they install it.
- **Ask once**, in the person's language, before preparing or using anything that costs them something. Say what it adds to this analysis and every cost: each download's size, the space on disk, the time, that it uses the network, any system package it needs (installing one changes the machine and usually needs administrator rights: on Debian and Ubuntu, the tool's virtual environment needs `python3-venv` and the hearing check needs `espeak-ng`; `check` says when one is missing), and whether it would send their audio or video to an outside service (the tool's own path sends nothing; a service you propose may, and so may your own model provider, which receives what you open). Take the tool's numbers from `check`, never from memory; for anything else, say what you know of its cost and what you do not. Nothing is forbidden: the person decides. Then wait for the answer.
- **Never prepare anything without a yes, and never carry on without saying what the result will lack.**
  - **Yes** to the tool's own path: run the commands `check` printed under "prepare it", in order (the model comes only with `transcribe --download`), define `rs` with the Python `check` names for afterwards, run `rs check VIDEO` again to see it ready, and go on.
  - **No**: go on without it, and tell the person once what the result will lack. Run `scan` without `--transcript`: the riffsheet then says the speech was not transcribed and why, and never that nobody speaks.
- **Which speech recognizer is your choice.** `scan` needs a word-timed transcript in the format `transcribe` writes (`references/TOOL.md`). The tool offers one tested path, `transcribe` (faster-whisper with the `small` model), and `references/TOOL.md` gives what its measurements found for it. You may use another recognizer, another model size or a transcript the person supplies; pass `--transcript-by "what made it"` to `scan` (a transcript `transcribe` made needs nothing). The riffsheet records what made the transcript, and says plainly when it was not the tool's tested path.
- **Means outside the tool.** When you establish a fact with anything the tool does not provide (another program, a service, a source you looked up), list it in the judgment file under `own_means` with what you used: the riffsheet marks it as established by your own means. When you need something and find no way to get it, record the gap under `tool_gaps`. `riffsheet.md` shows both.

## Sound: describe it only if you passed the hearing check

The tool cannot hear: it measures loudness and when sound events fall, not what a sound is. Some agents run on a model that takes sound as input; most do not, and what you believe about your own abilities is not evidence. So whether you can hear is settled for this analysis by a test the tool sets and marks:

1. After `scan`, when the video has an audio track: `rs hear-check DIR`. It writes a short sound file in which a voice says six digits.
2. Open `DIR/hearing/check_1.wav` (the file it names) the way you open the pictures: with the tool that reads a file into your input, the one that shows you an image. If your model takes sound as input, the file reaches you as sound: listen to it, then answer with the six digits you heard, in order, and nothing else: `rs hear-check DIR --answer DIGITS`. Answer `rs hear-check DIR --cannot-hear` only after trying, when opening the file gives you nothing to listen to (an error that the file type is not supported, raw bytes, or a description of the file in place of its sound). Not knowing whether you can hear is no reason to answer it: open the file first. For most agents `--cannot-hear` is the honest answer, and it costs the analysis nothing.
3. Never work the digits out by measuring the file (decoding it, a speech recognizer, a script, its waveform or spectrum): a check passed that way would make everything you later say about the sound an invention.
4. After a pass, `rs listen DIR` cuts the video's sound around each measured sound event, and the whole track when the video is short, into files: open them as sound, and write what you hear under `heard` in the judgment file (`references/METHOD.md`, section 6). Each statement goes out marked heard by the agent. The sound then reaches your model provider as the pictures do. Without a pass, `build` refuses `heard` statements and lists as a problem any other sentence that says what the sound is (music, a song, a sound effect, a tone of voice), wherever you wrote it, `own_means` and `tool_gaps` included; what the sound is stays under `cannot_judge`.

## How to do it

Follow `references/METHOD.md` from start to finish; read `references/TOOL.md` once for what each command prints and its limits. In short:

1. With the tool's speech recognition: `rs transcribe VIDEO --out T.json; rs scan VIDEO --out DIR --transcript T.json && rs build DIR` (a `;` after `transcribe`: if it fails, it leaves in T.json why, and `scan` records it, so the riffsheet says the speech recognition failed and why; tell the person). Without speech recognition: `rs scan VIDEO --out DIR && rs build DIR`. With a transcript made another way: `rs scan VIDEO --out DIR --transcript T.json --transcript-by "what made it"`.
2. Read the summary `scan` printed (no need to open `summary.txt` again), then open the overview sheets and any jump-cut sheet in one step. With an audio track, take the hearing check in the same step (above).
3. In one step, read every caption region with `text`, measure every graphic with `element`, and take the `zoom`, `frames`, `mouth` and `color` views the overview calls for. A full-frame end card over a still picture gets its times from `element` but no box: give that box by eye.
4. Write the judgment file, taking pace words from the PACE block of the step 1 sheet and wrapping every statement that uses a word from its DETAIL WORDS list, and run `build DIR --judgment J.json --out OUT`.
5. For every statement it lists, open a large view of that moment, compare your words with it, and name the view in the statement's mark; rebuild until it prints `CHECKS: all passed`. Until then it writes no riffsheet. `build` checks that each statement names a close view of its moment; whether the words match the picture is yours to check.

Batch independent commands and images into one step: each step costs a full re-read of the conversation.

Then report to the person (below), and say what the analysis lacks: anything that did not run or ran by other means, and whether the sound was heard (the paragraphs under the first line of `riffsheet.md`), and what it could not judge.

## Telling the person

`riffsheet.json` and `riffsheet.md` stay in English: they are what the tool's checks read. Do not write a translation of them unless asked. Report in your reply, in the person's language, the way a person wants to read it:

1. One plain line per shot, with its time, saying what is seen: who and what, doing what. Not how it is framed.
2. Why the video holds a viewer, and what their version has to keep.
3. What the analysis lacks, and where the files are.

Spoken lines and on-screen words stay in the video's own language, exactly as `riffsheet.md` gives them, in quotation marks; you may follow a quote with its meaning in their language in parentheses. Times and numbers are those of `riffsheet.md`.

Only when the person asks for the whole riffsheet in their language, write `riffsheet.<code>.md` beside the English files, where `<code>` is the two-letter code of their language (`riffsheet.zh.md`, `riffsheet.es.md`, `riffsheet.ja.md`). Rewrite it whenever `riffsheet.md` is rebuilt. It is your own writing: the tool neither writes nor checks it.

- The first line, in their language, says that it renders the checked English `riffsheet.md` beside it, which wins wherever the two differ (in Chinese, for example: 本文是同一文件夹里经过检查的英文版 riffsheet.md 的中文译本；两者不一致时，以 riffsheet.md 为准。).
- Everything in `riffsheet.md` is there, in the same order, in their language: the title line, the line under it, every paragraph, every heading, every beat and every list item. Nothing is summarized, added or left out.
- Unchanged, character for character: every time and time range (`00:02.4–00:04.1`, `2.375 s`), every number with its unit (`-10 dB`, `0 of 3 cuts`, `8.042 s`, `0.052 s`), and every spoken line and on-screen word in quotation marks, which stay in the video's own language exactly as `riffsheet.md` gives them (spelling, case, punctuation). You may follow a quote with its meaning in their language in parentheses.
- Names of files, commands and fields (`riffsheet.json`, `zoom`) stay as they are; ordinary English words, the pace and measure words among them (`measured`, `brisk`, `locked`), are translated.

## Making their own version

Section 11 of `references/METHOD.md` says what can be rebuilt with code or an editor, and where footage of people, places and products comes from: a camera or a video model. Riffkit (https://riffkit.ai/?utm_source=riffsheet&utm_medium=skill&utm_campaign=riffsheet&utm_content=skill_md) makes that footage from the original video.

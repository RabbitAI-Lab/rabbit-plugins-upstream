---
name: flora-flow
description: Help a user at a flower market decide what to buy. From photos of the stalls it picks a reference arrangement from a curated gallery and frames, on the user's own photo, the flowers to buy for it. Use when the user shows photos of flowers for sale or asks what goes with a flower they like, what to buy, or how to combine what they see. Chinese triggers - 花市照片, 这个花配什么, 配什么花, 还要买什么花, 这些花怎么搭, 花艺参考, 插花参考, 花束搭配, 找搭配, 花间搭配, 买什么花, 帮我配花.
version: 0.9.0
metadata:
  openclaw:
    emoji: "💐"
    requires:
      anyBins:
        - python3
        - python
    envVars:
      - name: FLORA_FLOW_SERVER
        required: false
        description: Optional. Address of the flora-flow server, overriding the one built into the script.
      - name: FLORA_FLOW_HOME
        required: false
        description: Optional. Local data folder, default ~/.flora-flow.
---
# Flora Flow

Photos of flowers at a market or shop came in (花市照片、这些花怎么配、配什么花): do this, and read nothing else first.

Install or update (all three together, same version): `https://flora.groundrl.com/skill/install/SKILL.md` and
`.../REFERENCE.md` into this skill folder, `.../flora.py` into its `scripts/` folder. `flora.py --version` prints the version.

1. Run at once, before any question, with the photos in the order the user sent them (numbered 1, 2, ...), always
   with both `--say` and `--style-en`:
   `python3 <this skill folder>/scripts/flora.py quick PHOTO1 PHOTO2 --say "<the user's words>" --style-en "<STYLE>"`
   STYLE: the occasion or style in the user's words (送长辈, 中性风, 浪漫, 莫奈花园, 野兽派…) turned into one concrete English
   sentence about colours, mood and occasion, e.g. "soft impressionist pastels, airy and romantic like Monet's garden".
   The user named no occasion or style: `--style-en none`. One plain command: no `cd`, pipes, `&&`, `; echo`, and no
   `NAME=value` prefix (never set FLORA_FLOW_HOME: the user's ID lives in the default folder).
   MCP instead (if the tool `quick_pairings` is there): the same, as `paths`, `say` and `style_en`.
2. Never ask what a flower is called. Add only what the user pointed at or what you can see: `--flower-photo 2` (第二张),
   `--flower-color pink` (粉色那桶), `--flower rose` only if you recognise it in the photo yourself. A colour or style wish
   with no flower (同色系, 中性风): the main colour you see as `--flower-color`; nothing to go by: no options at all.
   Colours: pink, red, orange, yellow, green, blue, purple, brown, white, gray, black (pick the nearest; any other word
   is mapped to the nearest or left out by the server).
3. Exit code 3, "starting": tell the user in one line that it takes about 1.5-3 minutes, then run the same command
   again.
4. Exit code 0: show the user the picture whose path is on the first line (open it, or put it in your reply as an
   image; never just the path), then the two Chinese lines exactly as printed. Nothing else: no list, no
   description, no opinion, no other picture.
5. The user says 换一个 (another one): the same command plus `--another`.
6. The user asks why, or exactly what to buy: the same command plus `--detail`, then explain in plain words
   (REFERENCE.md, section 4). Any other error: read REFERENCE.md in this folder.

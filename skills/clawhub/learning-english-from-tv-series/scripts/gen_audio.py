#!/usr/bin/env python3
"""DramaLex · gen_audio.py
为 words.json 中每个词/语块及原句生成 TTS 音频（离线优先）。支持后端：
  say (macOS 内置) / espeak-ng (Linux) / pyttsx3 (Windows/跨平台) / gTTS (在线)。
纯标准库 + 可选后端；更新 json 写入音频路径。Agent 中立。
"""
import argparse, json, os, re, shutil, subprocess, sys, time

def pick_backend(pref):
    if pref and pref != 'auto':
        return pref
    if shutil.which('say'):
        return 'say'
    if shutil.which('espeak-ng') or shutil.which('espeak'):
        return 'espeak'
    try:
        import pyttsx3
        pyttsx3.init()
        return 'pyttsx3'
    except Exception:
        pass
    try:
        import gtts
        return 'gtts'
    except Exception:
        pass
    return 'pyttsx3'

def say_to_wav(text, out_wav, voice='Samantha'):
    aiff = out_wav[:-4] + '.aiff'
    # macOS 语音合成服务在高频连续调用时偶发抢占失败 → 重试 + 退避，确保稳定产出
    ok = False
    for attempt in range(3):
        if os.path.exists(aiff):
            os.remove(aiff)
        r = subprocess.run(['say', '-v', voice, '-o', aiff, text], capture_output=True)
        if r.returncode == 0 and os.path.exists(aiff) and os.path.getsize(aiff) > 0:
            ok = True
            break
        time.sleep(0.3 * (attempt + 1))
    if not ok:
        return False
    # aiff -> wav via macOS built-in afconvert (aifc module removed in py3.13)
    rc = subprocess.run(['afconvert', '-f', 'WAVE', '-d', 'LEI16', aiff, out_wav], capture_output=True)
    if rc.returncode == 0 and os.path.exists(out_wav) and os.path.getsize(out_wav) > 0:
        os.remove(aiff)
        return True
    if os.path.exists(aiff):
        shutil.move(aiff, out_wav)
    return os.path.exists(out_wav) and os.path.getsize(out_wav) > 0

def espeak_to_wav(text, out_wav):
    exe = 'espeak-ng' if shutil.which('espeak-ng') else 'espeak'
    r = subprocess.run([exe, '--stdout', '-w', out_wav, text], capture_output=True)
    return r.returncode == 0 and os.path.exists(out_wav)

def pyttsx3_to_wav(text, out_wav):
    try:
        import pyttsx3
        e = pyttsx3.init()
        e.save_to_file(text, out_wav)
        e.runAndWait()
        return os.path.exists(out_wav)
    except Exception as e:
        print(f"pyttsx3 失败: {e}", file=sys.stderr)
        return False

def gtts_to_mp3(text, out_mp3):
    try:
        from gtts import gTTS
        gTTS(text=text, lang='en').save(out_mp3)
        return os.path.exists(out_mp3)
    except Exception as e:
        print(f"gTTS 失败: {e}", file=sys.stderr)
        return False

def gen(text, out_path, backend, voice):
    """返回实际生成的音频路径（含正确扩展名），失败返回空串。"""
    if backend == 'say':
        return out_path if say_to_wav(text, out_path, voice) else ""
    if backend == 'espeak':
        return out_path if espeak_to_wav(text, out_path) else ""
    if backend == 'pyttsx3':
        return out_path if pyttsx3_to_wav(text, out_path) else ""
    if backend == 'gtts':
        mp3 = out_path[:-4] + '.mp3'
        return mp3 if gtts_to_mp3(text, mp3) else ""
    return ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--media-dir', default='media')
    ap.add_argument('--backend', default='auto')
    ap.add_argument('--voice', default='Samantha')
    args = ap.parse_args()

    with open(args.input, encoding='utf-8') as f:
        words = json.load(f)
    os.makedirs(args.media_dir, exist_ok=True)
    backend = pick_backend(args.backend)
    print(f"TTS 后端: {backend}")

    for i, w in enumerate(words):
        base = f"{i+1:03d}_{re.sub(r'[^a-z0-9]+','_', w['term'].lower())}"
        twav = os.path.join(args.media_dir, base + '.wav')
        p = gen(w['term'], twav, backend, args.voice)
        if p:
            w['term_audio'] = p
        if w.get('line'):
            lwav = os.path.join(args.media_dir, base + '_line.wav')
            p2 = gen(w['line'], lwav, backend, args.voice)
            if p2:
                w['line_audio'] = p2
        # 让出语音合成服务，避免连续调用抢占失败
        time.sleep(0.15)

    with open(args.input, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"已为 {len(words)} 个条目生成音频 -> {args.media_dir}")

if __name__ == '__main__':
    main()

import argparse
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description="Clear X compose textarea (discards any draft text).")
    parser.parse_args()

    js = """
(() => {
  try {
    // Match the same prioritization as fill-compose: target the compose inside the visible dialog.
    let el = null;
    const modals = document.querySelectorAll('[role="dialog"]');
    for (const m of modals) {
      const t = m.querySelector('[data-testid="tweetTextarea_0"]');
      if (t && m.offsetParent !== null) { el = t; break; }
    }
    if (!el) el = document.querySelector('[data-testid="tweetTextarea_0"]');
    if (!el) return JSON.stringify({ cleared: false, message: 'compose textarea not found' });
    el.focus();
    document.execCommand('selectAll', false, null);
    el.dispatchEvent(new InputEvent('beforeinput', { inputType: 'deleteContentBackward', bubbles: true, cancelable: true }));
    document.execCommand('delete', false, null);
    el.dispatchEvent(new InputEvent('input', { inputType: 'deleteContentBackward', bubbles: true }));
    return JSON.stringify({ cleared: true, remaining: el.innerText });
  } catch (e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
"""
    print(js)


if __name__ == "__main__":
    main()

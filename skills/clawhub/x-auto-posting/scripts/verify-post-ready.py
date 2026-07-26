import argparse
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description=(
            "Verify the X compose is correctly filled and the Post button is enabled. "
            "Reads the compose textarea inside the visible modal (preferring the one with "
            "aria-labelledby=modal-header) and reports whether Draft.js has accepted the text."
        )
    )
    parser.parse_args()

    js = """
(() => {
  try {
    const modal = document.querySelector('[role="dialog"][aria-labelledby="modal-header"]');
    let scope = null;
    if (modal && modal.offsetParent !== null) {
      scope = modal;
    } else {
      const dialogs = document.querySelectorAll('[role="dialog"]');
      for (const d of dialogs) {
        if (d.offsetParent !== null && d.querySelector('[data-testid="tweetTextarea_0"]')) { scope = d; break; }
      }
    }
    if (!scope) scope = document;
    const el = scope.querySelector('[data-testid="tweetTextarea_0"]');
    const btn = scope.querySelector('[data-testid="tweetButton"]') || scope.querySelector('[data-testid="tweetButtonInline"]');
    const mediaCount = scope.querySelectorAll('[data-testid="attachments"] img, [data-testid="attachments"] video').length;
    if (!el) return JSON.stringify({ error: true, message: 'compose textarea not found' });
    const text = el.innerText || '';
    const disabled = btn ? btn.getAttribute('aria-disabled') === 'true' : true;
    return JSON.stringify({
      compose_text: text,
      compose_length: text.length,
      post_enabled: !disabled,
      post_button_found: !!btn,
      media_attached: mediaCount
    });
  } catch (e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
"""
    print(js)


if __name__ == "__main__":
    main()

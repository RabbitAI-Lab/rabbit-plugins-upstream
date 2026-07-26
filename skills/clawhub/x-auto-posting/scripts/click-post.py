import argparse
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description="Click the Post button in the X compose dialog and return the button state before the click."
    )
    parser.parse_args()

    js = """
(() => {
  try {
    // Same scope resolution as fill-compose: the Post button lives in the same container
    // as the compose the user filled. Picking the wrong container yields a disabled button
    // from the OTHER composer (modal vs sidebar).
    let scope = null;
    const modals = document.querySelectorAll('[role="dialog"]');
    for (const m of modals) {
      if (m.offsetParent !== null && m.querySelector('[data-testid="tweetTextarea_0"]')) {
        scope = m;
        break;
      }
    }
    if (!scope) scope = document;
    const btn = scope.querySelector('[data-testid="tweetButton"]')
             || scope.querySelector('[data-testid="tweetButtonInline"]')
             || document.querySelector('[data-testid="tweetButton"]')
             || document.querySelector('[data-testid="tweetButtonInline"]');
    if (!btn) return JSON.stringify({ clicked: false, message: 'post button not found' });
    const disabled = btn.getAttribute('aria-disabled') === 'true';
    if (disabled) return JSON.stringify({ clicked: false, message: 'post button disabled (empty text or unmet condition)', button_text: btn.textContent });
    btn.click();
    return JSON.stringify({ clicked: true, button_text: btn.textContent });
  } catch (e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
"""
    print(js)


if __name__ == "__main__":
    main()

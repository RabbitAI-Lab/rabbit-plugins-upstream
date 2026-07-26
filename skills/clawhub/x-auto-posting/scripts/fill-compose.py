import argparse
import json
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description="Fill the X compose textarea with the given tweet text.")
    parser.add_argument("text", help="Tweet body to insert (<= 280 chars for free accounts)")
    parser.add_argument("--stdin", action="store_true", help="Read text from stdin instead of argv")
    args = parser.parse_args()

    if args.stdin:
        text = sys.stdin.read()
    else:
        text = args.text

    text_json = json.dumps(text)

    js = f"""
(async () => {{
  try {{
    const text = {text_json};
    // X renders BOTH an inline composer (sidebar on /home) and a modal composer (on /compose/post).
    // The modal composer is the dialog with aria-labelledby="modal-header" -- prefer it explicitly.
    // Falling back to any visible dialog, then to a document-wide match.
    let el = null;
    let scope = null;  // the container holding the correct compose + its sibling Post button
    const modalHeader = document.querySelector('[role="dialog"][aria-labelledby="modal-header"]');
    if (modalHeader && modalHeader.offsetParent !== null) {{
      const t = modalHeader.querySelector('[data-testid="tweetTextarea_0"]');
      if (t) {{ el = t; scope = modalHeader; }}
    }}
    if (!el) {{
      const dialogs = document.querySelectorAll('[role="dialog"]');
      for (const m of dialogs) {{
        const t = m.querySelector('[data-testid="tweetTextarea_0"]');
        if (t && m.offsetParent !== null) {{ el = t; scope = m; break; }}
      }}
    }}
    if (!el) {{
      el = document.querySelector('[data-testid="tweetTextarea_0"]');
      scope = document;
    }}
    if (!el) return JSON.stringify({{ error: true, message: 'compose textarea not found -- navigate to x.com/compose/post or click the Post button in the sidebar first' }});

    el.focus();
    // Clear existing content.
    document.execCommand('selectAll', false, null);
    document.execCommand('delete', false, null);

    // Draft.js listens to `beforeinput` to update its internal ContentState.
    // Dispatching beforeinput + execCommand insertText + input makes the framework actually register the change
    // (not just visually update the DOM).
    el.dispatchEvent(new InputEvent('beforeinput', {{ inputType: 'insertText', data: text, bubbles: true, cancelable: true }}));
    document.execCommand('insertText', false, text);
    el.dispatchEvent(new InputEvent('input', {{ inputType: 'insertText', data: text, bubbles: true }}));

    await new Promise(r => setTimeout(r, 400));

    // The Post button lives in the same scope as the compose we just filled.
    // Modal compose -> [data-testid="tweetButton"] inside the dialog.
    // Sidebar/home inline compose -> [data-testid="tweetButtonInline"] in the main doc.
    // Checking scope first avoids reading the disabled sibling button from the other composer.
    const btn = scope.querySelector('[data-testid="tweetButton"]')
             || scope.querySelector('[data-testid="tweetButtonInline"]')
             || document.querySelector('[data-testid="tweetButton"]')
             || document.querySelector('[data-testid="tweetButtonInline"]');
    const filled = el.innerText || '';
    return JSON.stringify({{
      filled_text: filled,
      length: filled.length,
      post_enabled: btn ? btn.getAttribute('aria-disabled') !== 'true' : false,
      post_button_found: !!btn
    }});
  }} catch (e) {{
    return JSON.stringify({{ error: true, message: e.message }});
  }}
}})()
"""
    print(js)


if __name__ == "__main__":
    main()

import argparse
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description="Check if current X session is logged in.")
    parser.parse_args()

    js = """
(() => {
  try {
    // Desktop layout: sidebar account switcher + compose button
    const desktopSwitcher = document.querySelector('[data-testid="SideNav_AccountSwitcher_Button"]');
    // Mobile layout: profile icon in bottom nav + floating compose button
    const mobileProfile = document.querySelector('[data-testid="DashButton_ProfileIcon_Link"]');
    const loggedIn = !!(desktopSwitcher || mobileProfile);
    let username = null;
    let handle = null;
    if (desktopSwitcher) {
      username = desktopSwitcher.querySelector('[dir="ltr"] span span')?.textContent
              || desktopSwitcher.textContent?.trim()
              || null;
      handle = desktopSwitcher.querySelectorAll('[dir="ltr"]')?.[1]?.textContent || null;
    }
    return JSON.stringify({
      logged_in: loggedIn,
      username: username,
      handle: handle,
      url: location.href,
      title: document.title
    });
  } catch (e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
"""
    print(js)


if __name__ == "__main__":
    main()

export type IconName =
  | "arrow.down"
  | "arrow.down.circle.fill"
  | "captions.bubble.fill"
  | "chevron.down"
  | "clock.fill"
  | "cpu.fill"
  | "exclamationmark.triangle.fill"
  | "moon.fill"
  | "square.stack.3d.up.fill"
  | "sun.max.fill";

interface IconDefinition {
  sfSymbol: IconName;
  fallbackSymbol: string;
  svg: string;
}

const icons: Record<IconName, IconDefinition> = {
  "arrow.down": {
    sfSymbol: "arrow.down",
    fallbackSymbol: "arrow-down",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="M12 4.5v14m-5.5-5.5L12 19.5l5.5-6.5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" /></svg>',
  },
  "arrow.down.circle.fill": {
    sfSymbol: "arrow.down.circle.fill",
    fallbackSymbol: "download-circle",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="currentColor" /><path d="M12 7v9m-3.5-3.5L12 16l3.5-3.5" fill="none" stroke="var(--surface)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" /></svg>',
  },
  "captions.bubble.fill": {
    sfSymbol: "captions.bubble.fill",
    fallbackSymbol: "captions-bubble",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="M5.4 4.5h13.2A2.9 2.9 0 0 1 21.5 7.4v6.3a2.9 2.9 0 0 1-2.9 2.9h-7.2l-4.5 3v-3H5.4a2.9 2.9 0 0 1-2.9-2.9V7.4a2.9 2.9 0 0 1 2.9-2.9Z" fill="currentColor" /><path d="M7.3 9h9.4M7.3 12h6.3" fill="none" stroke="var(--surface)" stroke-linecap="round" stroke-width="1.6" /></svg>',
  },
  "chevron.down": {
    sfSymbol: "chevron.down",
    fallbackSymbol: "chevron-down",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="m6.5 9 5.5 5.5L17.5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" /></svg>',
  },
  "clock.fill": {
    sfSymbol: "clock.fill",
    fallbackSymbol: "clock",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="currentColor" /><path d="M12 7v5.5l3.5 2" fill="none" stroke="var(--surface)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" /></svg>',
  },
  "cpu.fill": {
    sfSymbol: "cpu.fill",
    fallbackSymbol: "cpu",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="M8 2.5v2m4-2v2m4-2v2M8 19.5v2m4-2v2m4-2v2M2.5 8h2m-2 4h2m-2 4h2m15.5-8h2m-2 4h2m-2 4h2" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.6" /><rect x="5" y="5" width="14" height="14" rx="3" fill="currentColor" /><rect x="8.5" y="8.5" width="7" height="7" rx="1.5" fill="var(--surface)" /></svg>',
  },
  "exclamationmark.triangle.fill": {
    sfSymbol: "exclamationmark.triangle.fill",
    fallbackSymbol: "warning-triangle",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="m10.6 3.8-8.4 14.4c-.7 1.2.2 2.8 1.6 2.8h16.4c1.4 0 2.3-1.6 1.6-2.8L13.4 3.8c-.7-1.2-2.1-1.2-2.8 0Z" fill="currentColor" /><path d="M12 8v5.2m0 3.5v.2" fill="none" stroke="var(--surface)" stroke-linecap="round" stroke-width="1.8" /></svg>',
  },
  "moon.fill": {
    sfSymbol: "moon.fill",
    fallbackSymbol: "moon",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><path d="M20.4 15.1A8.5 8.5 0 0 1 8.9 3.6 8.5 8.5 0 1 0 20.4 15.1Z" fill="currentColor" /></svg>',
  },
  "square.stack.3d.up.fill": {
    sfSymbol: "square.stack.3d.up.fill",
    fallbackSymbol: "batch-stack",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><rect x="7" y="3.5" width="13" height="10" rx="2" fill="currentColor" opacity=".42" /><rect x="5" y="7" width="13" height="10" rx="2" fill="currentColor" opacity=".7" /><rect x="3.5" y="10.5" width="13" height="10" rx="2" fill="currentColor" /></svg>',
  },
  "sun.max.fill": {
    sfSymbol: "sun.max.fill",
    fallbackSymbol: "sun",
    svg: '<svg class="ui-icon-svg" viewBox="0 0 24 24" focusable="false" aria-hidden="true"><circle cx="12" cy="12" r="3.5" fill="currentColor" /><path d="M12 2.5v2m0 15v2M4.8 4.8l1.4 1.4m11.6 11.6 1.4 1.4M2.5 12h2m15 0h2M4.8 19.2l1.4-1.4M17.8 6.2l1.4-1.4" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.7" /></svg>',
  },
};

function isIconName(value: string): value is IconName {
  return value in icons;
}

export function iconMarkup(name: IconName, className = ""): string {
  const definition = icons[name];
  const classes = className ? `ui-icon ${className}` : "ui-icon";
  return `<span class="${classes}" data-sf-symbol="${definition.sfSymbol}" data-fallback-symbol="${definition.fallbackSymbol}" aria-hidden="true">${definition.svg}</span>`;
}

export function setIcon(element: HTMLElement, name: IconName): void {
  const definition = icons[name];
  element.dataset.sfSymbol = definition.sfSymbol;
  element.dataset.fallbackSymbol = definition.fallbackSymbol;
  element.innerHTML = definition.svg;
  applyNativeIcon(element, name);
}

export function hydrateIcons(root: ParentNode = document): void {
  root.querySelectorAll<HTMLElement>("[data-sf-symbol]").forEach((element) => {
    const name = element.dataset.sfSymbol;
    if (name && isIconName(name)) setIcon(element, name);
  });
}

type NativeIconRenderer = (symbolName: IconName, target: HTMLElement) => boolean;

declare global {
  interface Window {
    subtitleVisualizerNativeIconRenderer?: NativeIconRenderer;
  }
}

function applyNativeIcon(element: HTMLElement, name: IconName): void {
  const renderer = window.subtitleVisualizerNativeIconRenderer;
  if (!renderer) return;
  if (renderer(name, element)) element.dataset.iconMode = "native";
  else delete element.dataset.iconMode;
}

export function applyNativeIcons(root: ParentNode = document): void {
  root.querySelectorAll<HTMLElement>("[data-sf-symbol]").forEach((element) => {
    const name = element.dataset.sfSymbol;
    if (name && isIconName(name)) applyNativeIcon(element, name);
  });
}

/**
 * SF Symbols are named native assets, so a browser cannot resolve them through
 * CSS alone. Keep the name as a stable semantic contract and render inline SVG
 * by default. A macOS native shell may provide this optional hook to replace
 * individual SVG fallbacks with NSImage-backed SF Symbols.
 */
export function setupIconSystem(): void {
  const platform = `${navigator.platform} ${navigator.userAgent}`;
  document.documentElement.dataset.iconPlatform = /Mac/i.test(platform) ? "macos" : "fallback";
  applyNativeIcons();
}

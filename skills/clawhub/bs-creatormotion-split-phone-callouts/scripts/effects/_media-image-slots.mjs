// Content imagery is resolved before composition authoring. Never replace a missing
// photograph, avatar or document with CSS bars, initials or geometric stand-ins.
export function imageSlot(ctx,key,alt='',className='content-image') {
  const source=ctx.images?.[key];
  if(!source) throw new Error(`Missing image slot "${key}". Supply it with --images or install the bundled default image assets.`);
  return `<img class="${ctx.esc(className)}" src="${ctx.esc(source)}" alt="${ctx.esc(alt)}" data-image-slot="${ctx.esc(key)}">`;
}

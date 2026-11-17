/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ['docs/**/*.html', 'docs/assets/*.js'],
  safelist: [
    'is-stuck', 'open', 'in', 'on', 'is-ready', 'zoomable', 'lb-lock', 'lang-zh',
    'border-ash-100/10', 'bg-ink-950/80', 'backdrop-blur-xl',
  ],
  theme: {
    extend: {
      colors: {
        ink: {
          950: '#070605',
          900: '#0c0b0a',
          850: '#12100e',
          800: '#1a1714',
          700: '#2a241f',
          600: '#3d342c',
        },
        ash: {
          100: '#f3eee6',
          200: '#e4dcd0',
          300: '#c9bdb0',
          400: '#9a8d80',
          500: '#6f655c',
        },
        ember: {
          300: '#f0b48a',
          400: '#e8915a',
          500: '#d4723a',
          600: '#b85a28',
        },
      },
      fontFamily: {
        display: ['"Syne"', '"HKW Sans SC"', 'system-ui', 'sans-serif'],
        sans: ['"HKW Sans SC"', '"Syne"', 'system-ui', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'ui-monospace', 'Menlo', 'monospace'],
      },
      boxShadow: {
        glow: '0 0 80px -20px rgba(212, 114, 58, 0.45)',
        panel: '0 24px 80px -32px rgba(0,0,0,0.75)',
      },
      backgroundImage: {
        'ember-radial':
          'radial-gradient(ellipse 80% 50% at 70% 0%, rgba(212,114,58,0.18), transparent 55%), radial-gradient(ellipse 60% 40% at 10% 80%, rgba(232,145,90,0.08), transparent 50%)',
        'grid-fade':
          'linear-gradient(to right, rgba(243,238,230,0.04) 1px, transparent 1px), linear-gradient(to bottom, rgba(243,238,230,0.04) 1px, transparent 1px)',
      },
      backgroundSize: {
        grid: '48px 48px',
      },
      animation: {
        'fade-up': 'fadeUp 0.7s ease-out both',
        'soft-pulse': 'softPulse 6s ease-in-out infinite',
        'orb-drift': 'orbDrift 16s ease-in-out infinite alternate',
      },
      keyframes: {
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(16px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        softPulse: {
          '0%, 100%': { opacity: '0.55' },
          '50%': { opacity: '1' },
        },
        orbDrift: {
          '0%': { transform: 'translate(0, 0) scale(1)' },
          '100%': { transform: 'translate(-4%, 6%) scale(1.08)' },
        },
      },
    },
  },
  plugins: [],
};

# Svelte + Flask

> [!TIP]
> Use mamba for both python and nodejs deps

## Requirements

- python
- flask
- nodejs
- pnpm

## Setup

Svelte's official and default way of setting up the app is with SvelteKit

```
pnpm create svelte@latest app
```

However we can go bit more minimal and just use vite

```
pnpm create vite app --template svelte
```

This will create a default minimal skeleton for the js side of things

For flask on the other hand we can just pick wherever we wanna have our stuff as we'll be defining the path for loading files in a relative way anyway - see `send_from_directory()` function in app.py.

While writing out svelte components, it's a lot more easier working with the vite dev server 

```
pnpm dev
```

Once ready for shipping n interation with python n stuff we can just build that stuff into dist

```
pnpm build
```

After which we just run flask

```
py app.py
```

There's prolly a way to do auto reload with npm watch or rollup or whatever, tbd

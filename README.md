# linkgap landing page

A static page: `index.html`, `style.css`, the screenshots in `img/`, the Inter font in
`fonts/` and `favicon.svg`. No build step, no JavaScript, no CDN, no analytics — it works
offline and every asset is served from this folder.

## Look at it locally

```bash
python3 site/preview.py     # http://127.0.0.1:8142
```

(Port 8142 on purpose: 8000 is the linkgap app itself.)

## Deploy to Netlify

`netlify.toml` sets the publish directory to this folder, so either route works:

**Drag and drop** — open <https://app.netlify.com/drop> and drop the `site` folder onto
the page. Netlify serves it immediately on a generated `*.netlify.app` address.

**CLI** — with the Netlify CLI installed and logged in (`npm i -g netlify-cli`,
`netlify login`):

```bash
cd site
netlify deploy          # draft URL, for checking
netlify deploy --prod   # publish it
```

The first `netlify deploy` in a folder asks which site to link or creates a new one.

## Updating the screenshots

The images in `img/` are cropped copies of `docs/screenshots/product/*.png`, one `-light`
and one `-dark` file per screen. The page picks the right one with `<picture>` and
`prefers-color-scheme`, so replace both files when a screen changes.

## Editing the copy

Every number on the page comes from `docs/DEMO.md` (the measured demo run). If the app's
numbers change, update them here too — and keep sample data labelled as sample.

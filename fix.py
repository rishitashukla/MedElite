with open('index.html', 'r') as f:
    content = f.read()

old = """  const fullUrl = `${base}?${params}`;
  const proxied = `https://corsproxy.io/?${encodeURIComponent(fullUrl)}`;
  return fetch(proxied).then(r => { if (!r.ok) throw new Error(`CMS ${r.status}`); return r.json(); });"""

new = """  const fullUrl = `${base}?${params}`;
  return fetch(fullUrl, { headers: { 'Origin': null } })
    .catch(() => fetch(`https://corsproxy.io/?${fullUrl}`))
    .then(r => { if (!r.ok) throw new Error(`CMS ${r.status}`); return r.json(); });"""

content = content.replace(old, new)
with open('index.html', 'w') as f:
    f.write(content)
print("Done")

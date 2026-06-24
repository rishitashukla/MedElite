with open('index.html', 'r') as f:
    content = f.read()

old = """function cmsQuery(resource, conditions, limit = 100) {
  const base = `https://data.cms.gov/provider-data/api/1/datastore/query/${resource}/0`;
  const params = new URLSearchParams();
  conditions.forEach((c, i) => {
    params.set(`conditions[${i}][property]`, c.property);
    params.set(`conditions[${i}][value]`, c.value);
    params.set(`conditions[${i}][operator]`, c.operator || '=');
  });
  params.set('limit', limit);
  const fullUrl = `${base}?${params}`;
  return fetch(fullUrl, { headers: { 'Origin': null } })
    .catch(() => fetch(`https://corsproxy.io/?${fullUrl}`))
    .then(r => { if (!r.ok) throw new Error(`CMS ${r.status}`); return r.json(); });
}"""

new = """async function cmsQuery(resource, conditions, limit = 100) {
  const filters = conditions.map((c, i) =>
    `conditions%5B${i}%5D%5Bproperty%5D=${encodeURIComponent(c.property)}&conditions%5B${i}%5D%5Bvalue%5D=${encodeURIComponent(c.value)}&conditions%5B${i}%5D%5Boperator%5D=%3D`
  ).join('&');
  const url = `https://data.cms.gov/provider-data/api/1/datastore/query/${resource}/0?${filters}&limit=${limit}`;
  const proxied = `https://corsproxy.io/?${encodeURIComponent(url)}`;
  const r = await fetch(proxied);
  if (!r.ok) throw new Error(`CMS ${r.status}`);
  return r.json();
}"""

content = content.replace(old, new)
with open('index.html', 'w') as f:
    f.write(content)
print("Done" if old in open('index.html').read() == False else "Replaced")

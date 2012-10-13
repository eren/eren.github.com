all: site

site: clean
	jekyll --no-server
	tree _site

clean:
	rm -rfv _site/*

server: site
	jekyll --server

require 'csv'

module Jekyll
    class IndexGenerator < Generator
        def generate(site)
            index = site.pages.detect {|page| page.name == "index.html"}
            index.data['books'] = CSV.read("./books.txt", {:col_sep => "|"})
            index.data['notes'] = site.posts.map {|post| post.data['book_id']}
        end
    end
end

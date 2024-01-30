#!/usr/bin/env ruby
# Regular expression which matches 10 digit phone num
puts ARGV[0].scan(/^[0-9]{10}$/).join


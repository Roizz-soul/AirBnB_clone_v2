# configuring my web servers using puppet

$word = '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'

$update = "\\\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}"

package { 'nginx':
	ensure   => 'present',
	provider => 'apt'
} ->

file { '/data/web_static/releases/test':
    ensure  => 'directory',
    recurse => true,
} ->

file { '/data/web_static/shared':
    ensure  => 'directory',
    recurse => true,
} ->

file { '/data/web_static/releases/test/index.html':
	ensure  => 'present',
	content => ${word},
} ->

file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test'
} ->

file { '/data':
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
}

exec { 'configure and restart nginx':
    command => 'sudo sed -i "55i $update" /etc/nginx/sites-available/default && 
                sudo service nginx restart',
    provider => shell,
}

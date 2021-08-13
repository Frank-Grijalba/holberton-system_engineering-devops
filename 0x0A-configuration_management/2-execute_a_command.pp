# kill a process with name killmenow

exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f ./killmenow',
}

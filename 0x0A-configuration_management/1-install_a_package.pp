# installs package puppet-lint: http://puppet-lint.com/

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}

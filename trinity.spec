%define	name	trinity
%define git	git5405bc7
%define	version 0.0.1git5405bc7

Summary: 	System calls fuzzer
Name: 		%{name}
Version: 	%{version}
Release: 	1
# generated by git archive --format=tar --prefix=trinity-git$(git describe --always)/ master | bzip2 > trinity-git$(git describe --always).tar.bz2
Source0:	%{name}-%{git}.tar.bz2
Patch0:		0001-Revert-2.6.39-specific-values.patch
URL: 		https://codemonkey.org.uk/projects/trinity/
License: 	GPLv2
Group: 		System/Servers 

%description
Trinity is a system call fuzzer which employs some
basic intelligence techniques (though when run without
any arguments it too is dumb as a rock).

The intelligence features include:

- If a system call expects a certain datatype as an
  argument (for example a file descriptor) it gets
  passed one.  This is the reason for the slow initial
  startup, as it generates a list of fd's of files it can
  read from /sys, /proc and /dev and then supplements
  this with fd's for various network protocol sockets.
  (Information on which protocols succeed/fail is cached
  on the first run, greatly increasing the speed of
  subsequent runs).

- If a system call only accepts certain values as an
  argument, (for example a 'flags' field), trinity has
  a list of all the valid flags that may be passed.  Just
  to throw a spanner in the works, occasionally, it will
  bitflip one of the flags, just to make things more
  interesting.

- If a system call only takes a range of values, the
  random value passed is ensured to fit within that
  range.

%prep
%setup -q -n %{name}-%{git}
%patch0 -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -m 755 -d %{buildroot}/%{_bindir}
%{__install} -Dm 644 %{name} %{buildroot}/%{_bindir}/%{name}

%{__install} -m 755 -d %{buildroot}/%{_datadir}/%{name}
%{__install} -Dm 644 bugs-found.txt %{buildroot}/%{_datadir}/%{name}/bugs-found.txt

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}/bugs-found.txt

Summary:	DevHelp book: gnomeui
Summary(pl):	Ksi±¿ka do DevHelp'a o gnomeui
Name:		devhelp-book-gnomeui
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gnomeui.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gnomeui

%description -l pl
Ksi±¿ka do DevHelp o gnomeui

%prep
%setup -q -c gnomeui -n gnomeui

%build
mv -f book gnomeui
mv -f book.devhelp gnomeui.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gnomeui
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gnomeui.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gnomeui/* $RPM_BUILD_ROOT%{_prefix}/books/gnomeui

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs

Summary:	DevHelp book: gnomeui
Summary(pl.UTF-8):	Książka do DevHelpa o gnomeui
Name:		devhelp-book-gnomeui
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gnomeui.tar.gz
# Source0-md5:	55a6920d719a965887d62d322e5747f6
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gnomeui.

%description -l pl.UTF-8
Książka do DevHelpa o gnomeui.

%prep
%setup -q -c -n gnomeui

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gnomeui,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gnomeui.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gnomeui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*

%global tl_name parrun
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typesets (two) streams of text running parallel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parrun
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
For typesetting translated text and the original source, parallel on the
same page, one above the other.


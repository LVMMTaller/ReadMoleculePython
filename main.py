import ReadMolecule

from rdkit.Chem import Draw
from PIL import Image
from rdkit import Chem

def print_info(mols):
    print(f'Num molecules:{len(mols)}')

    for i in range(len(mols)):
        print(f'Molecule {i} has {mols[i].GetNumAtoms()} atoms')

    mol = mols[0]

    # mol = Chem.AddHs(mol)

    print('For first molecule:')
    for i in range(mol.GetNumAtoms()):
        print(
            f'Atom {i} has symbol {mol.GetAtomWithIdx(i).GetSymbol()},'
            + f' valence {mol.GetAtomWithIdx(i).GetExplicitValence()} '
            + f'{"Is in Ring" if mol.GetAtomWithIdx(i).IsInRing() else "Is not in ring"}'
            + f' and {"Is an aromatic atom" if mol.GetAtomWithIdx(i).GetIsAromatic() else "Is not a aromatic atom"}')

    fig = Draw.MolToImage(mol, size=(300, 300))
    fig.show()


if __name__ == '__main__':
    csv_file = "DILI-Liew_2_B_TS_47.csv"
    sdf_file = '2_B_TS_47_act.sdf'

    print('mols from csv file')
    mols = ReadMolecule.read_smiles_from_csv(csv_file)

    print_info(mols)

    print('mols from sdf file')
    mols = ReadMolecule.read_sdf(sdf_file)

    print_info(mols)
